from utils.rcsv import *
import matplotlib.pyplot as plt

def compare_spectrum(spectrum_id0: str, spectrum_id1: str, offset: float = None):
    
    spectrum0 = read_spectrum(spectrum_id=spectrum_id0, get_info=False, dbm=True)[0]
    spectrum1 = read_spectrum(spectrum_id=spectrum_id1, get_info=False, dbm=True)[0]

    fig, ax = plt.subplots(1,1,figsize=(5,5),layout='constrained')
    ax.plot([float(key) for key in spectrum0.keys()], spectrum0.values())
    ax.plot([float(key) for key in spectrum1.keys()], [pwr+offset for pwr in spectrum1.values()])

    plt.show()


if '__main__' == __name__:
    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='CWDM_r0.5_s50', offset=0.0)
    
    # calibrated
    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_C_ri1.0_si50_ro0.03_so50', offset=0.0)

    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_C_ri0.5_si50_ro0.03_so50', offset=0.0)

    compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro1.0_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.5_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.2_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.1_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.07_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.05_so50', offset=0.0)
    compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_C_ri0.03_si50_ro0.03_so50', offset=0.0)
    
    # not calibrated
    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_!C_ri1.0_si50_ro0.03_so50', offset=0.0)
    #
    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_!C_ri0.5_si50_ro0.03_so50', offset=0.0)

    #compare_spectrum(spectrum_id0='CWDM_r1.0_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.5_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.2_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.1_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.07_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.05_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='CWDM_r0.03_s50', spectrum_id1='w0saCWDM_!C_ri0.03_si50_ro0.03_so50', offset=0.0)
    #
    #compare_spectrum(spectrum_id0='DWDM_r1.0_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.5_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.2_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.1_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.07_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.05_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.03_s50', spectrum_id1='w0saDWDM_!C_ri1.0_si50_ro0.03_so50', offset=0.0)
    #
    #compare_spectrum(spectrum_id0='DWDM_r1.0_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.5_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.2_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.1_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.07_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.05_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.03_s50', spectrum_id1='w0saDWDM_!C_ri0.5_si50_ro0.03_so50', offset=0.0)
    #
    #compare_spectrum(spectrum_id0='DWDM_r1.0_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro1.0_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.5_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.5_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.2_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.2_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.1_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.1_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.07_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.07_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.05_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.05_so50', offset=0.0)
    #compare_spectrum(spectrum_id0='DWDM_r0.03_s50', spectrum_id1='w0saDWDM_!C_ri0.03_si50_ro0.03_so50', offset=0.0)
