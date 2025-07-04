import numpy as np
import matplotlib.pyplot as plt
from w0sa.utils.conversions import *
from w0sa.utils.numeric import *
from w0sa.utils.spectrum_reader import *

def resample_spectrum(spectrum: dict, period: float = 6.25, freq: bool = False) -> dict:

    C = 299792458 # light speed m/s

    frecuencies = [Hz2THz(C/nm2m(float(wv))) for wv in spectrum.keys()] # THz
    resampled_frecuencies = [fq for fq in frange(int(frecuencies[-1]), int(frecuencies[0]+1), GHz2THz(period))] # THz

    interpoled_amplitude = np.interp(resampled_frecuencies, frecuencies[::-1], list(spectrum.values())[::-1])

    if freq:
        return {format_key(fq): amp for fq, amp in zip(resampled_frecuencies, interpoled_amplitude)}
    else:
        resampled_wavelengths = [m2nm(C/THz2Hz(fq)) for fq in resampled_frecuencies] # nm
        return {format_key(wv): amp for wv, amp in zip(resampled_wavelengths, interpoled_amplitude)}
    

if '__main__' == __name__:
    default_spectrum = read_spectrum(spectrum_id="default", get_info=False)[0]
    default_spectrum_resampled = resample_spectrum(spectrum=default_spectrum, period=6.25, freq=False)
    #print(default_spectrum_resampled)

    fig, ax = plt.subplots(1,1,figsize=(5,5), layout="constrained")
    ax.plot([float(key) for key in default_spectrum_resampled.keys()], default_spectrum_resampled.values())
    ax.plot([float(key) for key in default_spectrum.keys()], default_spectrum.values())
    plt.show()
