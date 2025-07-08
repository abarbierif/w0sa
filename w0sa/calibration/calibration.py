from w0sa.utils.numeric import *
from w0sa.utils.rcsv import *
from w0sa.utils.resample import *
from w0sa.utils.conversions import *
from w0sa.core.wss_simulator import WSSimulator
import numpy as np
import matplotlib.pyplot as plt


class Calibration:
    """
    Calibration class performs the necessary calibration process to reach real output data.
    """

    C = 299792458                                                               # m/s (light speed in air/vacuum) 

    _DEFAULT_RESOLUTION = 1.0                                                   # nm
    _DEFAULT_ATTENUATION = 5.0                                                  # dB


    def __init__(self):
        self.wss_wavelengths = [format_key(m2nm(Calibration.C/THz2Hz(float(fq)))) for fq in WSSimulator().frequencies[::-1]]
        self.attenuation = Calibration._DEFAULT_ATTENUATION

    def get_attenuation(self, in_res: float = None, out_res: float = None):
        """
        Computes the neccesary power calibration based on input resolution (EDFA resolution) and the desired OSA output resolution.
        """

        in_atn = 10*np.log10(Calibration._DEFAULT_RESOLUTION/in_res) if Calibration._DEFAULT_RESOLUTION >= in_res else 10*np.log10(in_res/Calibration._DEFAULT_RESOLUTION)
        out_atn = 10*np.log10(Calibration._DEFAULT_RESOLUTION/out_res) if Calibration._DEFAULT_RESOLUTION >= out_res else 10*np.log10(out_res/Calibration._DEFAULT_RESOLUTION)

        self.attenuation = Calibration._DEFAULT_ATTENUATION - in_atn + out_atn


if '__main__' == __name__:
    print(Calibration().get_default_attenuation())
    #print(Calibration().avg_atn)
    
    #def get_default_attenuation(self):

    #    for ids in CALIBRATION_DATA.values():
    #        osa_id = ids["osa"]
    #        w0sa_id = ids["w0sa"]
    #       
    #        osa_data = resample(spectrum=read_spectrum(spectrum_id=osa_id, get_info=False, dbm=True)[0])
    #        w0sa_data = resample(spectrum=read_spectrum(spectrum_id=w0sa_id, get_info=False, dbm=True)[0])

    #        for wv in self.wss_wavelengths:
    #            if wv in osa_data and wv in w0sa_data:
    #                diff = abs(osa_data[wv] - w0sa_data[wv])
    #            else:
    #                diff = None
    #            
    #            Calibrator._DEFAULT_ATTENUATION[wv].append(diff)

    #    for wv in Calibrator._DEFAULT_ATTENUATION.keys():
    #        Calibrator._DEFAULT_ATTENUATION[wv] = np.min(Calibrator._DEFAULT_ATTENUATION[wv])

    #    thresh = 2*np.mean(list(Calibrator._DEFAULT_ATTENUATION.values()))

    #    for wv in Calibrator._DEFAULT_ATTENUATION.keys():
    #        if Calibrator._DEFAULT_ATTENUATION[wv] > thresh:
    #            Calibrator._DEFAULT_ATTENUATION[wv] = np.min(Calibrator._DEFAULT_ATTENUATION.values())
