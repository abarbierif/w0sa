import numpy as np

def GHz2THz(ghz: float) -> float:
    return ghz / 1000

def THz2GHz(thz: float) -> float:
    return thz * 1000

def THz2Hz(thz: float) -> float:
    return thz * 1e+12

def m2nm(m: float) -> float:
    return m * 1e+09
