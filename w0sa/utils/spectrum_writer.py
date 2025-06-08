import csv
from datetime import datetime
from w0sa.utils.spectrum_inputs import *
import os
import numpy as np

def write_spectrum(spectrum: dict):
    
    date = datetime.now().strftime("%y%m%d")
    num = 0
    filename = 'w0sa' + date + '_' + str(num) + '.csv'
    filepath = os.path.join(SPECTRUMS_DIR, filename)
    while os.path.exists(filepath):
        num += 1
        filename = 'w0sa' + date + '_' + str(num) + '.csv'
        filepath = os.path.join(SPECTRUMS_DIR, filename)
    
    with open(filepath, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Wavelength(A)', 'Level(A)'])
        for wv, pwr in spectrum.items():
            writer.writerow([wv, pwr])

if '__main__' == __name__:
    spc = {str(_):np.random.randint(100) for _ in range(100)}
    write_spectrum(spectrum=spc) 
