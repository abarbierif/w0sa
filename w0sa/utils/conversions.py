import numpy as np

def GHz2THz(ghz: float) -> float:
    return ghz / 1000

def THz2GHz(thz: float) -> float:
    return thz * 1000

def THz2Hz(thz: float) -> float:
    return thz * 1e+12

def Hz2THz(hz: float) -> float:
    return hz / 1e+12

def m2nm(m: float) -> float:
    return m * 1e+09

def nm2m(nm: float) -> float:
    return nm / 1e+09

def mW2dBm(mw: float) -> float:
    return 10 * np.log10(mw)

def dBm2mW(dbm: float) -> float:
    return 10 ** (dbm / 10)
