import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.ndimage import gaussian_filter1d
from utils.conversions import *
from data.config_spectrums import INPUT_SPECTRUMS_DIR, OUTPUT_SPECTRUMS_DIR
from utils.numeric import *
from calibration.calibration import Calibration

class OSAmulator:

    C = 299792458                                                               # m/s (light speed in air/vacuum)
    
    # default configuration
    CENTER_WAVELENGTH = 1550                                                    # nm
    SPAN_WAVELENGTH = 50                                                        # nm
    START_WAVELENGTH = CENTER_WAVELENGTH - (SPAN_WAVELENGTH / 2)                # nm
    STOP_WAVELENGTH = CENTER_WAVELENGTH + (SPAN_WAVELENGTH / 2)                 # nm
    SAMPLING_POINTS = 501
    OUTPUT_RESOLUTION = 1.0                                                     # nm

    INPUT_RESOLUTION = 1.0                                                      # nm

    BIN_WIDTH = (STOP_WAVELENGTH - START_WAVELENGTH) / (SAMPLING_POINTS - 1)    # nm

    def __init__(self):
        self.center_wavelength = OSAmulator.CENTER_WAVELENGTH
        self.span_wavelength = OSAmulator.SPAN_WAVELENGTH
        self.start_wavelength = OSAmulator.START_WAVELENGTH
        self.stop_wavelength = OSAmulator.STOP_WAVELENGTH
        self.sampling_points = OSAmulator.SAMPLING_POINTS
        self.output_resolution = OSAmulator.OUTPUT_RESOLUTION
        self.input_resolution = OSAmulator.INPUT_RESOLUTION

        self.bin_width = OSAmulator.BIN_WIDTH

        self.calibrator = Calibration()
 
 
    def spanning(self, center: float = CENTER_WAVELENGTH, span: int = SPAN_WAVELENGTH, points: int = SAMPLING_POINTS):
        
        self_center_wavelength = center
        self.span_wavelength = span
        self.sampling_points = points

        self.start_wavelength = self.center_wavelength - (self.span_wavelength / 2)
        self.stop_wavelength = self.center_wavelength + (self.span_wavelength / 2)

        self.bin_width = (self.stop_wavelength - self.start_wavelength) / (self.sampling_points - 1)

    def resampling(self, data: dict = None):
        
        target_wavelength = [wv for wv in frange(self.start_wavelength, self.stop_wavelength+(self.bin_width/2), self.bin_width)]
        resampled_data = np.interp(target_wavelength, list(data.keys()), list(data.values()), left=np.min(list(data.values())), right=np.min(list(data.values())))

        return target_wavelength, resampled_data

    def smoothing(self, data: dict = None):
        
        #spacing = list(data.keys())[1] - list(data.keys())[0]
        #print(spacing)
        #sigma = (self.output_resolution/spacing)/2.355

        #pwr_smoothed = gaussian_filter1d(list(data.values()), sigma, mode='reflect')
        #return pwr_smoothed
        
        delta = list(data.keys())[1] - list(data.keys())[0]
        n_kernel = int(round(self.output_resolution/delta)) if int(round(self.output_resolution/delta))%2 else int(round(self.output_resolution/delta))+1
        #print(n_kernel)
        x = np.arange(n_kernel)-(n_kernel-1)/2
        #print(x.shape)
        sigma = (self.output_resolution/delta)/2.355
        #print(sigma)
        kernel = np.exp(-0.5*(x/sigma)**2)
        kernel /= kernel.sum()

        pwr_smoothed = np.convolve(list(data.values()), kernel, mode='same')
        return pwr_smoothed

    def set_inres(self, inres: float = None):
        self.input_resolution = inres
    
    def set_outres(self, outres: float = None):
        self.output_resolution = outres

    def apply_attenuation(self, data: list = None):

        self.calibrator.get_attenuation(in_res=self.input_resolution, out_res=self.output_resolution)
        
        return [pwr-self.calibrator.attenuation for pwr in data]
        #return data

    def show(self, data: dict = None, freq: bool = False, save: bool = False):

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
        power_attenuated = self.apply_attenuation(data=power_convolved_dbm)


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
