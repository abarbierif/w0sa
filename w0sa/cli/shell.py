import cmd
from w0sa.core.wss_simulator import WSSimulator
import numpy as np
import matplotlib.pyplot as plt
import os
from w0sa.utils.spectrum_inputs import SPECTRUM_INPUTS, SPECTRUM_DESCRIPTION
from w0sa.utils.conversions import *
import copy
from w0sa.utils.spectrum_writer import *

class W0SAShell(cmd.Cmd):
    intro = "Welcome to w0sa CLI. Type help or ? to list commands."
    prompt = "w0sa> "

    def __init__(self):
        super().__init__()
        self.sim = WSSimulator()
    
    def do_exit(self, arg):
        """EN: Exits the w0sa CLI.\nES: Sale de la interfaz de línea de comandos de w0sa.\n\n Example:\n > exit"""
        print("Exiting w0sa...")
        return True

    def do_clear(self, arg):
        """EN: Clears the terminal screen.\nES: Limpia la pantalla del terminal.\n\n Example:\n > clear"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_ls_spectrums(self, arg):
        """EN: Lists the available spectrums.\nES: Lista los espectros disponibles.\n\n Example:\n > ls_spectrums"""
        for spectrum in SPECTRUM_INPUTS.keys():
            print(f"{spectrum} -> {SPECTRUM_DESCRIPTION[spectrum]}")

    def do_ls_ports(self, arg):
        """EN: Lists current ports configuration.\nES: Lista la configuración actual de puertos.\n\n EXAMPLE:\n > ls_ports"""
        for port, port_config in self.sim.ports.items():
            print(f"{port} -> {port_config['spectrum_id']}")

    def do_OSA_SHOW(self, arg):
        """EN: Displays the optical spectrum measured by the simulated OSA (Optical Spectrum Analyzer).\nES: Muestra el espectro óptico medido por el OSA (Analizador de Espectro Óptico) simulado.\n\n - Syntax: OSA_SHOW [-wv | -freq]\n - -wv: Plot in wavelength (nm) [default]\n - -fq: Plot in frequency (THz)\n\n Example:\n > OSA_SHOW\n > OSA_SHOW -fq"""
        
        C = 299792458 # light speed m/s

        flags = set(arg.strip().split())

        if not flags.issubset({'-wv','-fq','-save'}):
            print("Error: invalid option(s)")
            return

        plt.style.use('dark_background')
        fig, ax = plt.subplots(1,1,layout='constrained',figsize=(5,5))
        fig.canvas.manager.set_window_title('Optical Spectrum Analyzer Viewer')
        ax.grid('on', linewidth=0.3)
                 
        
        if '-fq' in flags:
            x_spectrum = [float(fq) for fq in self.sim.spectrum.keys()]
            ax.set_xlabel("Frequency (THz)")
        else:
            x_spectrum = [m2nm(C/THz2Hz(float(fq))) for fq in list(self.sim.spectrum.keys())[::-1]] # nm
            ax.set_xlabel("$\lambda$ (nm)")
        
        y_spectrum = list(self.sim.spectrum.values())[::-1] if '-fq' not in flags else list(self.sim.spectrum.values())
        ## for i,j in zip(x_spectrum,y_spectrum):
        ##     print(i, j)

        ax.set_ylabel("Power (dBm)")
        ax.plot(x_spectrum, y_spectrum, color='y')

        plt.show()
        
        if '-save' in flags:
            x_spectrum = [str(m2nm(C/THz2Hz(float(fq)))) for fq in list(self.sim.spectrum.keys())[::-1]] # nm
            y_spectrum = list(self.sim.spectrum.values())[::-1]
            write_spectrum(spectrum={wv:dBm2mW(pwr) for wv,pwr in zip(x_spectrum,y_spectrum)})


    def do_SETP(self, arg):
        """EN: Sets the input spectrum (in dBm) of a WSS input port.\nES: Define el espectro de entrada (en dBm) de un puerto del WSS.\n\n - Syntax: set_port <port> -> <spectrum_id>\n - Ports: P1–P9\n - Type "ls_ports" to list available spectra (IDs)\n\n Example:\n > SETP P1 -> default\n > SETP P2 -> default"""
        
        if not arg.strip():
            print("Error: no assignments provided")
            return

        try:
            prt, sid = arg.split('->', 1)
            prt = prt.strip()
            sid = sid.strip()

            if prt not in self.sim.ports.keys():
                print(f"Error: invalid port {prt}. Valid ports: P1-P9.")
                return

            if sid not in SPECTRUM_INPUTS.keys():
                print(f"Error: invalid spectrum key {sid}. Use <lss> to list available spectra.")
                return

            self.sim.prt_pwr_set(prt=prt, sid=sid)

        except ValueError:
            print(f"Error: malformed assignment {arg} - expected: <port> -> <spectrum_id>.")
        except Exception as e:
            print(f"Unexpected error set_port {e}.")

    def do_DCC(self, arg):
        """EN: Defines slot ranges for each logical channel in the WSS.\nES: Define los rangos de slots para cada canal lógico en el WSS.\n\n - Syntax: <channel>=<start_slot>:<end_slot>; ...\n - Slot range: 1 to 386 (represents 386 12.5 GHz slots in C-band)\n - Channels can be assigned non-overlapping slot ranges\n\n Example:\n > DCC 1=90:93; 2=94:94\n > DCC 3=100:110"""

        if not arg.strip():
            print("Error: no assignments provided")
            return
        self.sim.channels = {}
        parts = [_.strip() for _ in arg.split(';') if _.strip()]
        for part in parts:
            try:
                ch, sl = part.split('=', 1)
                ch = int(ch)
                sli, slf = sl.split(':', 1)
                sli = int(sli)
                slf = int(slf)
                
                self.sim.dcc_set(ch=ch, sli=sli, slf=slf)

            except ValueError:
                print(f"Error: malformed assignment {part} - expected: <channel>=<slot_i>:<slot_f>")
            except Exception as e:
                print(f"Error in slot {part}: {e}")

    def do_DCCS(self, arg):
        """EN: Displays the current channel configuration status.\nES: Muestra el estado actual de la configuración de canales.\n\n - Syntax: DCCS\n - Shows channel-slot mapping as <channel>=<start_slot>:<end_slot>\n\n Example:\n > DCCS\n 1=90:93; 2=94:94"""
        
        status = ''
        for ch,ch_config in self.sim.channels.items():
            status += str(ch) + '=' + str(ch_config['sli']) + ':' + str(ch_config['slf']) + ';'

        print(status[:-1])

    def do_URA(self, arg):
        """EN: Assigns an input port to a logical channel and applies attenuation in dB.\nES: Asocia un puerto de entrada a un canal lógico y aplica una atenuación en dB.\n\n - Syntax: <channel>,<port>,<attenuation>; ...\n - Channels must have been previously defined via `DCC`\n - Ports: 1–9\n - Attenuation: 0.0 (no loss) to 20.0 (max suppression)\n\n Example:\n > URA 1,1,0.0; 2,1,20.0\n > URA 3,2,10.5"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        parts = [_.strip() for _ in arg.split(';') if _.strip()]
        for part in parts:
            try:
                ch, prt, atn = part.split(',', 2)
                ch = int(ch)
                prt = 'P' + str(int(prt))
                atn = float(atn)
                
                self.sim.ura_set(ch=ch, prt=prt, atn=atn)

            except ValueError:
                print(f"Error: malformed assignment {part} - expected: <channels>,<port>,<attenuation>")
            except Exception as e:
                print(f"Error in slot {part}: {e}")

    def do_RSW(self, arg):
        """EN: Updates the WSS with the reconfigured channel plan.\nES: Actualiza el WSS con el plan de canales reconfigurado.\n\nExample: > RSW"""
        
        self.sim.channels_status = copy.deepcopy(self.sim.channels)
        self.sim.spectrum = {}
        self.sim.get_spectrum()

    def do_URAS(self, arg):
        """EN: Displays the current channel configuration status.\nES: Muestra el estado actual de la configuración de canales.\n\n - Syntax: URAS\n - Shows channel-slot mapping as <channel>,<port>,<attenuation>\n\n Example:\n > URAS\n 1,1,0.0;2,1,20.0"""

        status = ''
        for ch,ch_config in self.sim.channels_status.items():
            status += str(ch) + ',' + (str(ch_config['prt'])[1:] if ch_config['prt'] is not None else str(ch_config['prt'])) + ',' + str(ch_config['atn']) + ';'

        print(status[:-1])
