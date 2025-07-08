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
    if mw <= 0:
        return 10 * np.log10(1e-12)
    else:
        return 10 * np.log10(mw)

def dBm2mW(dbm: float) -> float:
    return 10 ** (dbm / 10)

def uW2dBm(uw: float) -> float:
    mw = uw / 1000
    return mW2dBm(mw=mw)

def dBm2uW(dbm: float) -> float:
    return (10 ** (dbm / 10)) * 1000

if '__main__' == __name__:
    mw = 201.1
    print(mW2dBm(mw=mw), 'dB')
    print()
    #print(uW2dBm(uw=201.1), 'dBm')
    print(mW2dBm(mw=201.1), 'dB')
    print(mW2dBm(mw=606.67), 'dB')
    #print(dBm2uW(dbm=23.03), 'mW')
    print(dBm2mW(dbm=23.03))
    print(dBm2mW(dbm=27.82))
