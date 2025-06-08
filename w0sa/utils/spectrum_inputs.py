import os

SPECTRUMS_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "spectrums")

SPECTRUM_INPUTS = {
    "default": os.path.join(SPECTRUMS_DIR, "WaveData20240829_004.csv"),
    "DWDM": os.path.join(SPECTRUMS_DIR, "WaveData20240906_002.csv"),
    "CWDM": os.path.join(SPECTRUMS_DIR, "WaveData20240906_001.csv"),
    "w0saDWDM": os.path.join(SPECTRUMS_DIR, "w0sa250607_0.csv"),
    "w0saCWDM": os.path.join(SPECTRUMS_DIR, "w0sa250607_1.csv"),
    # future entries here
}

SPECTRUM_DESCRIPTION = {
    "default": "Output spectrum of an EDFA at a maximum pump current of 1000[mA].",
    "DWDM": "Dense Wavelength Division Multiplexing (DWDM).",
    "CWDM": "Coarse Wavelength Division Multiplexing (CWDM).",
    "w0saDWDM": "w0sa version of DWDM.",
    "w0saCWDM": "w0sa version of CWDM.",
    # future entries here
}
