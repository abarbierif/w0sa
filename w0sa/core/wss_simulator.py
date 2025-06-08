import numpy as np
from w0sa.utils.conversions import *
from w0sa.utils.numeric import *
from w0sa.utils.spectrum_reader import *
from w0sa.utils.spectrum_resample import *
import copy

class WSSimulator:

    MAX_PORTS = 9
    CHANNEL_BANDWIDTH = 12.5                # GHz (flexigrid)
    WSS_RESOLUTION = CHANNEL_BANDWIDTH / 2
    SLOTS_NUM = 386 
    MAX_CHANNEL_POWER = 27.0                # dBm
    MAX_SLOT_POWER = 9.0                    # dBm
    MAX_ATTENUATION = 20.0                  # dBm
    MIN_ATTENUATION = 0.0                    # dBm

    C = 299792458                           # light speed m/s

    # wavelength[m] = C[m/s] / freq[Hz]
    MIN_FREQ   = 191.300000                 # THz
    MAX_FREQ   = 196.100000                 # THz

    # visualization params
    SPECTRUM_MARGIN = 50

    def __init__(self):
        self.spectrum = {}
        self.frecuencies = [format_key(_) for _ in frange(WSSimulator.MIN_FREQ-GHz2THz(WSSimulator.WSS_RESOLUTION), WSSimulator.MAX_FREQ+GHz2THz(WSSimulator.WSS_RESOLUTION), GHz2THz(WSSimulator.WSS_RESOLUTION))] # THz
        
        self.slots = {sl:{'fqi':self.frecuencies[fq],'fqc':self.frecuencies[fq+1],'fqf':self.frecuencies[fq+2]} for sl,fq in zip(range(1,WSSimulator.SLOTS_NUM+1),range(0,len(self.frecuencies)-2,2))}
        
        self.none_spectrum = {fq:0.0 for fq in self.frecuencies}
        self.ports = {'P'+str(_):{'spectrum_id':None,'spectrum':None} for _ in range(1,WSSimulator.MAX_PORTS+1)}

        self.channels = {ch:{'sli':sli,'slf':sli+3,'prt':None,'atn':None} for ch,sli in zip(range(1,97),range(1,382,4))} # default channels plan
        self.channels_status = copy.deepcopy(self.channels) # for status commands

    def prt_pwr_set(self, prt: int, sid: float):
        self.ports[prt]['spectrum_id'] = sid
        self.ports[prt]['spectrum'] = resample_spectrum(spectrum=read_spectrum(spectrum_id=sid, get_info=False)[0], freq=True)

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
                    fq_pwr = source_spectrum[fq] - atn
                    if fq_pwr > WSSimulator.MAX_SLOT_POWER:
                        print(f"WARNING: MAX SLOT POWER ({WSSimulator.MAX_SLOT_POWER}) EXCEEDED AT {fq} THz: {fq_pwr}")

                    self.spectrum[fq] = fq_pwr

            #for sl in range(self.channels[ch]['sli'], self.channels[ch]['slf']+1):
            #    for fq in self.slots[sl].keys():
            #        if self.ports[self.channels[ch]['prt']] == None:
            #            if WSSimulator.MIN_ATTENUATION <= self.channels[ch]['atn'] <= WSSimulator.MAX_ATTENUATION:
            #                if self.none_spectrum[self.slots[sl][fq]] - self.channels[ch]['atn'] <= WSSimulator.MAX_SLOT_POWER:
            #                    self.spectrum[self.slots[sl][fq]] = self.none_spectrum[self.slots[sl][fq]] - self.channels[ch]['atn']
            #                else:
            #                    self.spectrum[self.slots[sl][fq]] = self.none_spectrum[self.slots[sl][fq]] - self.channels[ch]['atn']
            #                    print(f"WARNING: MAX SLOT POWER ({WSSimulator.MAX_SLOT_POWER}) EXCEEDED: {self.spectrum[self.slots[sl][fq]]}")
            #            else:
            #                self.spectrum[self.slots[sl][fq]] = self.none_spectrum[self.slots[sl][fq]] - WSSimulator.MAX_ATTENUATION
            #                print(f"WARNING: MAX ATTENUATION ({WSSimulator.MAX_ATTENUATION}) EXCEEDED: MAX ATTENUATION WAS APPLIED TO FREQUENCY {self.slots[sl][fq]}")
            #        else:
            #            if WSSimulator.MIN_ATTENUATION <= self.channels[ch]['atn'] <= WSSimulator.MAX_ATTENUATION:
            #                if self.ports[self.channels[ch]['prt']][self.slots[sl][fq]] - self.channels[ch]['atn'] <= WSSimulator.MAX_SLOT_POWER:
            #                    self.spectrum[self.slots[sl][fq]] = self.ports[self.channels[ch]['prt']][self.slots[sl][fq]] - self.channels[ch]['atn']
            #                else:
            #                    self.spectrum[self.slots[sl][fq]] = self.ports[self.channels[ch]['prt']][self.slots[sl][fq]] - self.channels[ch]['atn']
            #                    print(f"WARNING: MAX SLOT POWER ({WSSimulator.MAX_SLOT_POWER}) EXCEEDED: {self.spectrum[self.slots[sl][fq]]}")
            #            else:
            #                self.spectrum[self.slots[sl][fq]] = self.ports[self.channels[ch]['prt']][self.slots[sl][fq]] - WSSimulator.MAX_ATTENUATION 
            #                print(f"WARNING: MAX ATTENUATION ({WSSimulator.MAX_ATTENUATION}) EXCEEDED: MAX ATTENUATION WAS APPLIED TO FREQUENCY {self.slots[sl][fq]}")
                

if '__main__' == __name__:
    #print(WSSimulator().frecuencies)
    #print(WSSimulator().slots)
    pass
