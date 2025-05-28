import numpy as np
from w0sa.utils.conversions import *
from w0sa.utils.numeric import *

class WSSimulator:

    MAX_PORTS = 9
    MAX_CHANNEL_POWER = 27.0

    C = 299792458 # light speed m/s

    # wavelength[m] = C[m/s] / freq[Hz]
    MIN_FREQ   = 191.3000 # THz
    MAX_FREQ   = 196.1000 # THz
    #MIN_WVL    = 1530.0   # nm
    #MAX_WVL    = 1570.0   # nm

    # visualization params
    SPECTRUM_MARGIN = 50

    def __init__(self, ch_bw='flexigrid'):
        self.ch_bw = 12.5 if ch_bw=='flexigrid' else ch_bw # channel bandwidth in GHz
        self.n_slots = (round((round(WSSimulator.MAX_FREQ-WSSimulator.MIN_FREQ,1)/GHz2THz(self.ch_bw)))+2) if self.ch_bw==12.5 else round((round(WSSimulator.MAX_FREQ-WSSimulator.MIN_FREQ,1)/GHz2THz(self.ch_bw)))
        self.spectrum = {}
        self.frecuencies = [round(_,4) for _ in frange(WSSimulator.MIN_FREQ-(WSSimulator.SPECTRUM_MARGIN*GHz2THz(self.ch_bw)), WSSimulator.MAX_FREQ+(WSSimulator.SPECTRUM_MARGIN*GHz2THz(self.ch_bw)), GHz2THz(self.ch_bw))] # THz
        self.wavelengths = [round(m2nm(WSSimulator.C/THz2Hz(f)),4) for f in self.frecuencies] # nm
        
        self.slots = {}
        for sl in range(1,self.n_slots+1):
            self.slots[sl] = 0.0

        self.ports = {_:0.0 for _ in range(WSSimulator.MAX_PORTS+1)}

        self.channels = {ch:{'sli':sli,'slf':sli+3,'pwr':0.0} for ch,sli in zip(range(1,97),range(1,382,4))} # generalize

    def prt_pwr_set(self, prt: int, pwr: float):
        self.ports[prt] = pwr

    def dcc_set(self, ch: int, sli: int, slf: int):
        self.channels[ch] = {'sli':sli, 'slf':slf, 'pwr':0.0}

    def ura_set(self, ch: int, pwr: float):
        self.channels[ch]['pwr'] = pwr

    def slots_set(self):
        for ch in self.channels:
            for sl in range(self.channels[ch]['sli'], self.channels[ch]['slf']+1):
                self.slots[sl] = self.channels[ch]['pwr']

    def get_spectrum(self, x_spectrum: float):
        self.slots_set()
        
        if x_spectrum == 'wv':
            for _ in range(WSSimulator.SPECTRUM_MARGIN):
                self.spectrum[self.wavelengths[_]] = 0.0
            _ = 0
            while _ < self.n_slots-1:
                self.spectrum[self.wavelengths[_+WSSimulator.SPECTRUM_MARGIN]] = self.slots[_+1]
                self.spectrum[self.wavelengths[_+WSSimulator.SPECTRUM_MARGIN+1]] = self.slots[_+1]
                _ += 1
            for _ in range(self.n_slots+WSSimulator.SPECTRUM_MARGIN,len(self.wavelengths)):
                self.spectrum[self.wavelengths[_]] = 0.0
        elif x_spectrum == 'freq':
            for _ in range(WSSimulator.SPECTRUM_MARGIN):
                self.spectrum[self.frecuencies[_]] = 0.0
            _ = 0
            while _ < self.n_slots-1:
                self.spectrum[self.frecuencies[_+WSSimulator.SPECTRUM_MARGIN]] = self.slots[_+1]
                self.spectrum[self.frecuencies[_+WSSimulator.SPECTRUM_MARGIN+1]] = self.slots[_+1]
                _ += 1
            for _ in range(self.n_slots+WSSimulator.SPECTRUM_MARGIN,len(self.frecuencies)):
                self.spectrum[self.frecuencies[_]] = 0.0

        #Add noise
        alpha = 0.1 #noise factor
        alpha_margin = 0.8 # noise factor for margins (visualization)
        
        for n,(key,noise) in enumerate(zip(self.spectrum.keys(),np.random.normal(size=len(self.spectrum)))):
            if n < WSSimulator.SPECTRUM_MARGIN or n >= len(self.spectrum)-WSSimulator.SPECTRUM_MARGIN:
                self.spectrum[key] = (1-alpha_margin)*self.spectrum[key] + alpha_margin*noise
            else:
                self.spectrum[key] = (1-alpha)*self.spectrum[key] + alpha*noise
                

if '__main__' == __name__:
    pass
