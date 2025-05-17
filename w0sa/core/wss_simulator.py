class WSSimulator():
    def __init__(self):
        self.channels = {}

    def dcc_set(self, ch, wl, pwr):
        self.channels[ch] = {'wavelength': wl, 'power': pwr}
