from utils.rcsv import *
import matplotlib.pyplot as plt
from utils.numeric import *

def get_spectral_density(data: dict = None):

    #wavelengths = np.array(sorted(map(float, data.keys())))
    #print(wavelengths)
    #powers = np.array([data[format_key(wv)] for wv in wavelengths])

    #deltas = np.diff(wavelengths)
    #print(deltas)
    #delta = deltas[0]
    #print(delta)
    
    wavelengths = [float(wv) for wv in data.keys()]
    print(len(wavelengths))

    delta = (wavelengths[-1] - wavelengths[0]) / (len(wavelengths) - 1)
    print(delta)

    densities = [pwr/delta for pwr in data.values()]

    return  dict(zip(wavelengths, densities))

if '__main__' == __name__:
    edfa_r10_s50 = read_spectrum(spectrum_id="EDFA1000_r1.0_s50", get_info=False, dbm=False)[0]
    dens_r10_s50 = get_spectral_density(data=edfa_r10_s50)
    edfa_r10_s100 = read_spectrum(spectrum_id="EDFA1000_r1.0_s100", get_info=False, dbm=False)[0]
    dens_r10_s100 = get_spectral_density(data=edfa_r10_s100)

    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    ax.plot(dens_r10_s50.keys(), dens_r10_s50.values())
    ax.plot(dens_r10_s100.keys(), dens_r10_s100.values())
    plt.show()
