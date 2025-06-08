import csv
from w0sa.utils.spectrum_inputs import SPECTRUM_INPUTS
from w0sa.utils.conversions import *
import matplotlib.pyplot as plt

def read_spectrum(spectrum_id: str = "default", get_info: bool = False):
    
    info = {}
    spectrum = {}
    is_data = False

    with open(SPECTRUM_INPUTS[spectrum_id], 'r') as file:
        spectrum_reader = csv.reader(file)
        for row in spectrum_reader:
            if row:
                if not is_data:
                    if len(row) == 3:
                        info[row[0]] = row[1] + ' ' + row[2] if row[2].strip() else row[1]
                    elif len(row) == 2:
                        info[row[0]] = row[1]
                else:
                    spectrum[row[0]] = mW2dBm(float(row[1]))
    
                if row[0] == 'Wavelength(A)':
                    is_data = True

    return spectrum, info if get_info else spectrum
    
        # test
        #for k,v in zip(info.keys(),info.values()):
        #    print(k,v)
    
        #print()
    
        #for k,v in zip(spectrum.keys(),spectrum.values()):
        #    print(k,v)

if "__main__" == __name__:
    #spectrum, info = read_spectrum(get_info=True)
    #print(spectrum, info)
    spectrum = read_spectrum(spectrum_id="CWDM", get_info=False)[0]
    #print(spectrum)

    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    ax.plot([float(key) for key in spectrum.keys()], spectrum.values())
    plt.show()
