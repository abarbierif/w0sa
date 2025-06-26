import numpy as np
from utils.conversions import *
from utils.numeric import *
from utils.rcsv import *
from utils.resample import *
from utils.dcc_generator import *
from utils.ura_generator import *
from utils.get_spectral_density import *
import copy

class WSSimulator:

    MAX_PORTS = 9
    CHANNEL_BANDWIDTH = 12.5                # GHz (flexigri)
    WSS_RESOLUTION = CHANNEL_BANDWIDTH / 2
    SLOTS_NUM = 386 
    MAX_CHANNEL_POWER = 27.0                # dBm
    MAX_SLOT_POWER = 9.0                    # dBm
    MAX_ATTENUATION = 20.0                  # dBm
    MIN_ATTENUATION = 0.0                   # dBm

    C = 299792458                           # light speed m/s

    # wavelength[m] = C[m/s] / freq[Hz]
    MIN_FREQ   = 191.300000 #191.375000                 # THz (datasheet: 191.300000)
    MAX_FREQ   = 196.100000 #196.200000                 # THz (datasheet: 196.100000)


    def __init__(self):
        self.spectrum = {}
        
        self.frequencies = [format_key(_) for _ in frange(WSSimulator.MIN_FREQ+(6*GHz2THz(WSSimulator.CHANNEL_BANDWIDTH)), WSSimulator.MAX_FREQ+(8*GHz2THz(WSSimulator.CHANNEL_BANDWIDTH)), GHz2THz(WSSimulator.WSS_RESOLUTION))] # THz
        
        self.slots = {sl:{'fqi':self.frequencies[fq],'fqc':self.frequencies[fq+1],'fqf':self.frequencies[fq+2]} for sl,fq in zip(range(1,WSSimulator.SLOTS_NUM+1),range(0,len(self.frequencies)-2,2))}
        
        self.none_spectrum = {fq:0.0 for fq in self.frequencies}
        self.ports = {'P'+str(_):{'spectrum_id':None,'spectrum':None} for _ in range(1,WSSimulator.MAX_PORTS+1)}
        
        self.channels = {ch:{'sli':sli,'slf':sli+3,'prt':None,'atn':None} for ch,sli in zip(range(1,97),range(1,382,4))} # default channels plan
        self.channels_status = copy.deepcopy(self.channels) # for status commands


    def prt_pwr_set(self, prt: int, sid: float):
        self.ports[prt]['spectrum_id'] = sid
        self.ports[prt]['spectrum'] = resample(spectrum=read_spectrum(spectrum_id=sid, get_info=False, dbm=False)[0], freq=True)

    def dcc_set(self, ch: int, sli: int, slf: int):
        if ch not in self.channels:
            self.channels[ch] = {'sli':sli,'slf':slf,'prt':None,'atn':0.0}
        else:
            self.channels[ch]['sli'] = sli
            self.channels[ch]['slf'] = slf

    def ura_set(self, ch: int, prt: str, atn: float):
        self.channels[ch]['prt'] = prt
        self.channels[ch]['atn'] = atn

    def get_spectrum(self):

        for ch,ch_config in self.channels.items():
            prt = ch_config['prt'] 
            atn = ch_config['atn']

            if atn and atn < WSSimulator.MIN_ATTENUATION:
                print(f"WARNING: MIN ATTENUATION ({WSSimulator.MIN_ATTENUATION}) EXCEEDED IN CHANNEL {ch}")
                #atn = WSSimulator.MIN_ATTENUATION
            elif atn and atn > WSSimulator.MAX_ATTENUATION:
                print(f"WARNING: MAX ATTENUATION ({WSSimulator.MAX_ATTENUATION}) EXCEEDED IN CHANNEL {ch}")
                #atn = WSSimulator.MAX_ATTENUATION

            source_spectrum = self.none_spectrum if self.ports[prt]['spectrum_id'] is None else self.ports[prt]['spectrum']

            for sl in range(ch_config['sli'], ch_config['slf']+1):
                slot = self.slots.get(sl)
                for fq in slot.values():
                    fq_pwr = source_spectrum[fq] * 10**(-atn/10)
                    if fq_pwr > WSSimulator.MAX_SLOT_POWER:
                        print(f"WARNING: MAX SLOT POWER ({WSSimulator.MAX_SLOT_POWER}) EXCEEDED AT {fq} THz: {fq_pwr}")

                    self.spectrum[fq] = fq_pwr

    def get_dcc(self):
        print(dcc_gen())

    def get_ura(self, spectrum_id: str = None):

        center_frequencies = [format_key(_) for _ in frange(WSSimulator.MIN_FREQ-GHz2THz(WSSimulator.WSS_RESOLUTION), WSSimulator.MAX_FREQ+GHz2THz(WSSimulator.WSS_RESOLUTION), GHz2THz(WSSimulator.CHANNEL_BANDWIDTH))] # THz
        
        out_spectrum = resample(spectrum=read_spectrum(spectrum_id=spectrum_id, get_info=False)[0], freq=True)
        ports = []
        attenuations = []
        for fq in center_frequencies:
            pwr_diffs = {}
            for prt,prt_config in self.ports.items():
                if prt_config['spectrum_id'] is not None:
                    prt_pwr = prt_config['spectrum'][fq]
                    out_pwr = out_spectrum[fq]
                    if prt_pwr > out_pwr:
                        pwr_diff = abs(prt_pwr - out_pwr)
                        pwr_diffs[prt] = pwr_diff

            prt = min(pwr_diffs, key=pwr_diffs.get)
            atn = pwr_diffs[prt]

            ports.append(prt[-1])
            attenuations.append(atn)

        ura_command = ura_gen(channels=386,ports=ports,attenuations=attenuations)

        print(ura_command)


if '__main__' == __name__:
    print(WSSimulator().frequencies)
    print(WSSimulator().slots)
    ## get_ura testing ##
    #sim = WSSimulator()
    #sim.prt_pwr_set(prt='P2',sid='default')
    #sim.get_ura(spectrum_id='CWDM')
    #sim.get_dcc()
