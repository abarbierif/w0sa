from w0sa.utils.spectrum_reader import *
import matplotlib.pyplot as plt

def compare_spectrum(spectrum_id0: str, spectrum_id1: str):
    
    spectrum0 = read_spectrum(spectrum_id=spectrum_id0, get_info=False)[0]
    spectrum1 = read_spectrum(spectrum_id=spectrum_id1, get_info=False)[0]

    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    ax.plot([float(key) for key in spectrum0.keys()], spectrum0.values())
    ax.plot([float(key) for key in spectrum1.keys()], spectrum1.values())

    plt.show()


if '__main__' == __name__:
    compare_spectrum(spectrum_id0='DWDM', spectrum_id1='w0saDWDM')
