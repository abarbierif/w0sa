from w0sa.utils.conversions import *
from w0sa.data.config_spectrums import INPUT_SPECTRUMS_DIR, OUTPUT_SPECTRUMS_DIR
from w0sa.utils.numeric import *
from w0sa.calibration.calibration import Calibration
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.ndimage import gaussian_filter1d

class OSAmulator:
    """
    OSAmulator manages everything related with visualization.
    """

    C = 299792458                                                               # m/s (light speed in air/vacuum)

    def __init__(self, center_wavelength=1550.0, span_wavelength=50.0, sampling_points=501, output_resolution=1.0, input_resolution=1.0):
        self.center_wavelength = center_wavelength
        self.span_wavelength = span_wavelength
        self.start_wavelength = center_wavelength - (span_wavelength / 2)
        self.stop_wavelength = center_wavelength + (span_wavelength / 2)
        self.sampling_points = sampling_points
        self.output_resolution = output_resolution #OSA resolution
        self.input_resolution = input_resolution

        self.bin_width = (self.stop_wavelength - self.start_wavelength) / (sampling_points - 1)

        self.calibrator = Calibration()
 
 
    def spanning(self, center: float = 1550.0, span: int = 50.0, points: int = 501):
        """
        Modifies OSA visualization parameters: center, span, sampling points.
        """
        
        self_center_wavelength = center
        self.span_wavelength = span
        self.sampling_points = points

        self.start_wavelength = self.center_wavelength - (self.span_wavelength / 2)
        self.stop_wavelength = self.center_wavelength + (self.span_wavelength / 2)

        self.bin_width = (self.stop_wavelength - self.start_wavelength) / (self.sampling_points - 1)

    def resampling(self, data: dict = None):
        """
        Resamples data according to the sampling points.
        """
        
        target_wavelength = [wv for wv in frange(self.start_wavelength, self.stop_wavelength+(self.bin_width/2), self.bin_width)]
        resampled_data = np.interp(target_wavelength, list(data.keys()), list(data.values()), left=np.min(list(data.values())), right=np.min(list(data.values())))

        return target_wavelength, resampled_data

    def smoothing(self, data: dict = None):
        """
        Performs a convolution between a 1D Gaussian kernel and the spectrum to handle OSA resolution.
        """

        delta = list(data.keys())[1] - list(data.keys())[0]
        fwhm_bins = self.output_resolution / delta
        sigma_bins = fwhm_bins / 2.355
        truncate = (round(fwhm_bins) - 1)/2 / sigma_bins #truncate=radius/sigma

        pwr_smoothed = gaussian_filter1d(
            list(data.values()),
            sigma=sigma_bins,
            mode='constant', 
            cval=0.0,
            truncate=truncate,
            radius=int((round(fwhm_bins)-1)/2)
        )
        
        #delta = list(data.keys())[1] - list(data.keys())[0]
        #n_kernel = int(round(self.output_resolution/delta)) if int(round(self.output_resolution/delta))%2 else int(round(self.output_resolution/delta))+1
        ##print(n_kernel)
        #x = np.arange(n_kernel)-(n_kernel-1)/2
        ##print(x.shape)
        #sigma = (self.output_resolution/delta)/2.355
        ##print(sigma)
        #kernel = np.exp(-0.5*(x/sigma)**2)
        #kernel /= kernel.sum()

        #pwr_smoothed = np.convolve(list(data.values()), kernel, mode='same')
        return pwr_smoothed

    def set_inres(self, inres: float = None):
        """
        Defines input resolution. Input resolution must match the input spectrum resolution. By default input resolution is 1.0 nm.
        """

        self.input_resolution = inres
    
    def set_outres(self, outres: float = None):
        """
        Defines the disired OSA output resolution. Default value is 1.0 nm.
        """

        self.output_resolution = outres

    def apply_attenuation(self, data: list = None):
        """
        Calls the calibrator object and applies power calibration to the spectrum.
        """

        self.calibrator.get_attenuation(in_res=self.input_resolution, out_res=self.output_resolution)
        
        return [pwr-self.calibrator.attenuation for pwr in data]
        #return data

    def show(self, data: dict = None, freq: bool = False, save: bool = False):
        """
        Main method of OSAmulator. This is intended to show the resulting spectrum.\n

        Data flow:\n

        1. Get resulting spectrum from WSSimulator.\n
        2. Convert frequencies to wavelengths.\n
        3. Apply Gaussian filter to manage resolution.\n
        4. Convert power from mW to dBm.\n
        5. Apply calibration.\n
        6. Resampling the data based on the sampling points.
        """

        plt.style.use('dark_background')
        fig, ax = plt.subplots(1,1,layout='constrained',figsize=(5,5))
        fig.canvas.manager.set_window_title('Optical Spectrum Analyzer Viewer')
        ax.grid('on', linewidth=0.3)
 
        # to wavelengths by default for resampling
        wavelengths = [m2nm(OSAmulator.C/THz2Hz(float(fq))) for fq in list(data.keys())[::-1]] # nm
        power_mw = list(data.values())[::-1]
        ax.set_xlabel("$\lambda$ (nm)")

        power_convolved_mw = self.smoothing(data=dict(zip(wavelengths, power_mw))) # gaussian filter
        power_convolved_dbm = [mW2dBm(pwr_mw) for pwr_mw in power_convolved_mw]
        power_attenuated = self.apply_attenuation(data=power_convolved_dbm) # calibration


        if freq:
            x_data = [Hz2THz(OSAmulator.C/nm2m(float(wv))) for wv in wavelengths[::-1]] # nm
            ax.set_xlabel("Frequency (THz)")
        else:
            x_data = wavelengths

        y_data = power_attenuated[::-1] if freq else power_attenuated
        x_data_resampled, y_data_resampled = self.resampling(data=dict(zip(x_data, y_data)))
        
        ax.set_ylabel("Power (dBm)")
        
        # debug
        #ax.plot([float(key) for key in data.keys()], data.values(), color='y')
        #ax.plot(wavelengths, power_mw, color='y')
        #ax.plot(wavelengths, power_convolved_mw, color='y')
        #ax.plot(wavelengths, power_convolved_dbm, color='y')
        ax.plot(x_data_resampled, y_data_resampled, color='y')

        plt.show()

        if save:
            if freq:
                x_data_resampled = [m2nm(OSAmulator.C/THz2Hz(float(fq))) for fq in x_data_resampled[::-1]] # nm
            
            self.write(data=dict(zip(x_data_resampled, y_data_resampled)))

    
    def write(self, data: dict = None):
        """
        Stores the output spectrum as a csv file in w0sa/data/output_spectrum directory.
        """
        
        date = datetime.now().strftime("%y%m%d")
        num = 0
        filename = 'w0sa' + date + '_' + str(num) + '.csv'
        filepath = os.path.join(OUTPUT_SPECTRUMS_DIR, filename)
        while os.path.exists(filepath):
            num += 1
            filename = 'w0sa' + date + '_' + str(num) + '.csv'
            filepath = os.path.join(OUTPUT_SPECTRUMS_DIR, filename)

        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(['File', filename[:-4]])
            writer.writerow(['',''])
            writer.writerow(['Center Wavelength', str(self.center_wavelength)])
            writer.writerow(['Span Wavelength', str(self.span_wavelength)])
            writer.writerow(['Start Wavelength', str(self.start_wavelength)])
            writer.writerow(['Stop Wavelength', str(self.stop_wavelength)])
            writer.writerow(['Resolution', str(self.output_resolution)])
            writer.writerow(['Sampling Points', str(self.sampling_points)])
            writer.writerow(['',''])
            writer.writerow(['Wavelength(A)', 'Level(A)'])

            for wv, pwr in data.items():
                writer.writerow([wv, dBm2mW(pwr)])

        print(filepath)

if '__main__' == __name__:
    OSAmulator().resampling()
