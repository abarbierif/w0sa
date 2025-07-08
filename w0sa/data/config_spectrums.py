import os

INPUT_SPECTRUMS_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "input_spectrums")
OUTPUT_SPECTRUMS_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "output_spectrums")

INPUT_SPECTRUMS = {
    # OSA
    "EDFA1000_r1.0_s45": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240829_004.csv"),
    "EDFA1000_r1.0_s75": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_002.csv"),
    
    "EDFA1000_r1.0_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_003.csv"),
    "EDFA1000_r0.5_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_004.csv"),
    "EDFA1000_r0.2_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_005.csv"),
    "EDFA1000_r0.1_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_006.csv"),
    "EDFA1000_r0.07_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_007.csv"),
    "EDFA1000_r0.05_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_008.csv"),
    "EDFA1000_r0.03_s50": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_009.csv"),
    
    "EDFA1000_r1.0_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_010.csv"),
    "EDFA1000_r0.5_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_011.csv"),
    "EDFA1000_r0.2_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_012.csv"),
    "EDFA1000_r0.1_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_013.csv"),
    "EDFA1000_r0.07_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_014.csv"),
    "EDFA1000_r0.05_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_015.csv"),
    "EDFA1000_r0.03_s100": os.path.join(INPUT_SPECTRUMS_DIR, "WaveData20240823_016.csv"),
    # future entries here
}

OUTPUT_SPECTRUMS = {
    # OSA
    "DWDM_r1.0_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_007.csv"),
    "DWDM_r0.5_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_008.csv"),
    "DWDM_r0.2_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_009.csv"),
    "DWDM_r0.1_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_010.csv"),
    "DWDM_r0.07_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_011.csv"),
    "DWDM_r0.05_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_012.csv"),
    "DWDM_r0.03_s35": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_013.csv"),
    
    "CWDM_r1.0_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_000.csv"),
    "CWDM_r0.5_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_001.csv"),
    "CWDM_r0.2_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_002.csv"),
    "CWDM_r0.1_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_003.csv"),
    "CWDM_r0.07_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_004.csv"),
    "CWDM_r0.05_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_005.csv"),
    "CWDM_r0.03_s60": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_006.csv"),
    
    "EDFA-WSS_r1.0_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_027.csv"),
    "EDFA-WSS_r0.5_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_026.csv"),
    "EDFA-WSS_r0.2_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_025.csv"),
    "EDFA-WSS_r0.1_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_024.csv"),
    "EDFA-WSS_r0.07_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_023.csv"),
    "EDFA-WSS_r0.05_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_022.csv"),
    "EDFA-WSS_r0.03_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240911_021.csv"),
    
    "DWDM_r1.0_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_017.csv"),
    "DWDM_r0.5_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_018.csv"),
    "DWDM_r0.2_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_019.csv"),
    "DWDM_r0.1_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_020.csv"),
    "DWDM_r0.07_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_021.csv"),
    "DWDM_r0.05_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_022.csv"),
    "DWDM_r0.03_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_023.csv"),
    
    "DWDM_r1.0_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_024.csv"),
    "DWDM_r0.5_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_025.csv"),
    "DWDM_r0.2_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_026.csv"),
    "DWDM_r0.1_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_027.csv"),
    "DWDM_r0.07_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_028.csv"),
    "DWDM_r0.05_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_029.csv"),
    "DWDM_r0.03_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_030.csv"),
    
    "CWDM_r1.0_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_031.csv"),
    "CWDM_r0.5_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_032.csv"),
    "CWDM_r0.2_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_033.csv"),
    "CWDM_r0.1_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_034.csv"),
    "CWDM_r0.07_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_035.csv"),
    "CWDM_r0.05_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_036.csv"),
    "CWDM_r0.03_s50": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_037.csv"),
    
    "CWDM_r1.0_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_038.csv"),
    "CWDM_r0.5_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_039.csv"),
    "CWDM_r0.2_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_040.csv"),
    "CWDM_r0.1_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_042.csv"),
    "CWDM_r0.07_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_042.csv"),
    "CWDM_r0.05_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_043.csv"),
    "CWDM_r0.03_s100": os.path.join(OUTPUT_SPECTRUMS_DIR, "WaveData20240823_044.csv"),
    
    #w0sa
    #"w0saDWDM_ri1.0_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250620_0.csv"),
    #"w0saCWDM_ri1.0_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250620_1.csv"),
    #"w0saCWDM_ri1.0_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250621_0.csv"),
    
    # !C means not calibrated
    "w0saCWDM_!C_ri1.0_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_0.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_1.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_2.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_3.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_4.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_5.csv"),
    "w0saCWDM_!C_ri1.0_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_6.csv"),

    "w0saCWDM_!C_ri0.5_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_7.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_8.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_9.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_10.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_11.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_12.csv"),
    "w0saCWDM_!C_ri0.5_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_13.csv"),
    
    "w0saCWDM_!C_ri0.03_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_28.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_29.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_30.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_31.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_32.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_33.csv"),
    "w0saCWDM_!C_ri0.03_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_34.csv"),

    "w0saDWDM_!C_ri1.0_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_14.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_15.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_16.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_17.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_18.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_19.csv"),
    "w0saDWDM_!C_ri1.0_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_20.csv"),

    "w0saDWDM_!C_ri0.5_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_21.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_22.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_23.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_24.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_25.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_26.csv"),
    "w0saDWDM_!C_ri0.5_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_27.csv"),
    
    "w0saDWDM_!C_ri0.03_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_35.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_36.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_37.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_38.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_39.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_40.csv"),
    "w0saDWDM_!C_ri0.03_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_41.csv"),

    # C means calibrated
    "w0saCWDM_C_ri1.0_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_42.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_43.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_44.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_45.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_46.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_47.csv"),
    "w0saCWDM_C_ri1.0_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_48.csv"),
    
    "w0saCWDM_C_ri0.5_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_49.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_50.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_51.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_52.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_53.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_54.csv"),
    "w0saCWDM_C_ri0.5_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_55.csv"),

    "w0saCWDM_C_ri0.03_si50_ro1.0_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_56.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.5_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_57.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.2_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_58.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.1_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_59.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.07_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_60.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.05_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_61.csv"),
    "w0saCWDM_C_ri0.03_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250623_62.csv"),

    "scipyw0saCWDM_C_ri1.0_si50_ro0.03_so50": os.path.join(OUTPUT_SPECTRUMS_DIR, "w0sa250707_0.csv"),
    # future entries here
}

SPECTRUM_DESCRIPTION = {
    "default": "Output spectrum of an EDFA at a maximum pump current of 1000[mA].",
    # future entries here
}
