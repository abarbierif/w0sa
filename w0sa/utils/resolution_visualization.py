from w0sa.utils.rcsv import *
import matplotlib.pyplot as plt

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
    pass
