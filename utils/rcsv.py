import csv
from data.config_spectrums import INPUT_SPECTRUMS, OUTPUT_SPECTRUMS
from utils.conversions import *
from utils.numeric import *
import matplotlib.pyplot as plt

def read_spectrum(spectrum_id: str = "default", get_info: bool = False, dbm: bool = False):
    
    info = {}
    spectrum = {}
    is_data = False
    csv_file = INPUT_SPECTRUMS[spectrum_id] if spectrum_id in INPUT_SPECTRUMS else OUTPUT_SPECTRUMS[spectrum_id]

    with open(csv_file, 'r') as file:
        spectrum_reader = csv.reader(file)
        for row in spectrum_reader:
            if row:
                if not is_data:
                    if len(row) == 3:
                        info[row[0]] = row[1] + ' ' + row[2] if row[2].strip() else row[1]
                    elif len(row) == 2:
                        info[row[0]] = row[1]
                else:
                    spectrum[row[0]] = mW2dBm(float(row[1])) if dbm else float(row[1])
    
                if row[0] == 'Wavelength(A)' or is_numeric(row[0]):
                    is_data = True

    return spectrum, info if get_info else spectrum
    

if "__main__" == __name__:
    spectrum = read_spectrum(spectrum_id="DWDM_r1.0_s50", get_info=False, dbm=True)[0]

    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    ax.plot([float(key) for key in spectrum.keys()], spectrum.values())
    plt.show()
