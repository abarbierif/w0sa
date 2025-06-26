import matplotlib.pyplot as plt
from utils.rcsv import *

def res_vis(spectrums_ids: list = None):

    plt.style.use('dark_background')
    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    fig.canvas.manager.set_window_title('Optical Spectrum Analyzer Viewer')
    ax.set_ylabel("Power (dBm)")
    ax.set_xlabel("$\lambda$ (nm)")
    ax.grid('on', linewidth=0.3)
    for spectrum_id in spectrums_ids:
        spectrum = read_spectrum(spectrum_id=spectrum_id, get_info=False)[0]
        spectrum_label = spectrum_id.split('_')[1]+'nm' if spectrum_id.split('_') else spectrum_id.split('_')[0]
        ax.plot([float(wv) for wv in spectrum.keys()], spectrum.values(), label=spectrum_label)
    
    ax.legend()
    plt.show()

if '__main__' == __name__:
    DWDM_ids = ["DWDM_1.0", "DWDM_0.5", "DWDM_0.2", "DWDM_0.1", "DWDM_0.07", "DWDM_0.05", "DWDM_0.03"]
    CWDM_ids = ["CWDM_1.0", "CWDM_0.5", "CWDM_0.2", "CWDM_0.1", "CWDM_0.07", "CWDM_0.05", "CWDM_0.03"]
    EDFA_WSS_ids = ["EDFA-WSS_1.0", "EDFA-WSS_0.5", "EDFA-WSS_0.2", "EDFA-WSS_0.1", "EDFA-WSS_0.07", "EDFA-WSS_0.05", "EDFA-WSS_0.03"]
    #EDFA_ids = ["EDFA_1.0", "EDFA_0.5", "EDFA_0.2", "EDFA_0.1", "EDFA_0.07", "EDFA_0.05", "EDFA_0.03"]
    comp = ["DWDM_1.0", "w0saDWDM_ri1.0_si50_ro1.0_so35"]
    res_vis(spectrums_ids=comp)
