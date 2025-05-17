import cmd
from w0sa.core.wss_simulator import WSSimulator

class W0SAShell(cmd.Cmd):
    intro = "Welcome to w0sa CLI. Type help or ? to list commands."
    prompt = "w0sa> "

    def __init__(self):
        super().__init__()
        self.sim = WSSimulator()
    
    def do_exit(self, arg):
        """Exit the w0sa CLI"""
        print("Exiting w0sa...")
        return True

    def do_dcc(self, line):
        """dcc <channel> <wavelength_nm> <power_dBm>"""
        try:
            ch, wl, pwr = line.split()
            self.sim.dcc_set(int(ch), float(wl), float(pwr))
            print(f"Set channel {ch} to {wl} nm @ {pwr} dBm")
        except Exception as e:
            print(f"Error: {e}")
