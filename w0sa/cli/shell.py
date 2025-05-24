import cmd
from w0sa.core.wss_simulator import WSSimulator
import numpy as np
import matplotlib.pyplot as plt
import os

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

    def do_osa_show(self, arg):
        """EN: Displays the optical spectrum measured by the simulated OSA (Optical Spectrum Analyzer).\nES: Muestra el espectro óptico medido por el OSA (Analizador de Espectro Óptico) simulado.\n\n - Syntax: osa_show [-wv | -freq]\n - -wv: Plot in wavelength (nm) [default]\n - -freq: Plot in frequency (THz)\n\n Example:\n > osa_show\n > osa_show -freq"""

        if arg.strip() not in ['','-wv','-freq']:
            print("Error: invalid option")
        else:
            plt.style.use('dark_background')
            fig, ax = plt.subplots(1,1,layout='constrained',figsize=(5,5))
            fig.canvas.manager.set_window_title('Optical Spectrum Analyzer Viewer')
            ax.grid('on', linewidth=0.3)
            self.sim.spectrum = {}
                 
            if not arg.strip() or arg.strip() == '-wv':
                self.sim.get_spectrum(x_spectrum='wv')
                x_spectrum, y_spectrum = list(self.sim.spectrum.keys())[::-1], list(self.sim.spectrum.values())[::-1]
                ax.set_xlabel("$\lambda$ (nm)")
            elif arg.strip() == '-freq':
                self.sim.get_spectrum(x_spectrum='freq')
                x_spectrum, y_spectrum = self.sim.spectrum.keys(), self.sim.spectrum.values()
                ax.set_xlabel("Frequency (THz)")

            # for i,j in zip(x_spectrum,y_spectrum):
            #     print(i, j)

            ax.set_ylabel("Power (dBm)")
            ax.plot(x_spectrum, y_spectrum, color='y')

            plt.show()

    def do_set_prt(self, arg):
        """EN: Sets the input power (in dBm) of a WSS input port.\nES: Define la potencia de entrada (en dBm) de un puerto del WSS.\n\n - Syntax: <port>:<power>\n - Ports: 1–9\n - Power range: 0 to 27 dBm\n\n Example:\n > set_prt 1:10.3\n > set_prt 2:2.7"""
        
        if not arg.strip():
            print("Error: no assignments provided")
            return

        try:
            prt, pwr = arg.split(':', 1)
            prt = int(prt)
            pwr = float(pwr)

            if not (1 <= prt <= self.sim.MAX_PORTS):
                print(f"Error: port {prt} out of valid range (1-9)")
                return

            if not (pwr < self.sim.MAX_CHANNEL_POWER):
                print(f"Warning: Power {pwr} dBm exceeds max recommended (27 dBm)")

            self.sim.prt_pwr_set(prt=prt, pwr=pwr)

        except ValueError:
            print(f"Error: malformed assignment {arg} - expected: <port>:<power>")
        except Exception as e:
            print(f"Unexpected error set_prt {e}")

    def do_dcc(self, arg):
        """EN: Defines slot ranges for each logical channel in the WSS.\nES: Define los rangos de slots para cada canal lógico en el WSS.\n\n - Syntax: <channel>=<start_slot>:<end_slot>; ...\n - Slot range: 1 to 386 (represents 386 12.5 GHz slots in C-band)\n - Channels can be assigned non-overlapping slot ranges\n\n Example:\n > dcc 1=90:93; 2=94:94\n > dcc 3=100:110"""

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

    def do_dcc_status(self, arg):
        """EN: Displays the current channel configuration status.\nES: Muestra el estado actual de la configuración de canales.\n\n - Syntax: dcc_status\n - Shows channel-slot mapping as <channel>=<slot_i>:<slot_f>\n\n Example:\n > dcc_status\n 1=90:93; 2=94:94"""
        status = ''
        for i in self.sim.channels:
            status += str(i) + '='
            for j in self.sim.channels[i]:
                if j == 'slf':
                    if i != list(self.sim.channels.keys())[-1]:
                        status += str(self.sim.channels[i][j]) + '; '
                    else:
                        status += str(self.sim.channels[i][j])
                elif j == 'sli':
                    status += str(self.sim.channels[i][j]) + ':'

        print(status)

    def do_ura(self, arg):
        """EN: Assigns an input port to a logical channel and applies attenuation in dB.\nES: Asocia un puerto de entrada a un canal lógico y aplica una atenuación en dB.\n\n - Syntax: <channel>,<port>,<attenuation>; ...\n - Channels must have been previously defined via `dcc`\n - Ports: 1–9\n - Attenuation: 0.0 (no loss) to ∞ (full suppression)\n\n Example:\n > ura 1,1,0.0; 2,1,20.0\n > ura 3,2,10.5"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        parts = [_.strip() for _ in arg.split(';') if _.strip()]
        for part in parts:
            try:
                ch, prt, atn = part.split(',', 2)
                ch = int(ch)
                prt = int(prt)
                atn = float(atn)
                
                pwr = self.sim.ports[prt] - atn
                self.sim.ura_set(ch=ch, pwr=pwr)

            except ValueError:
                print(f"Error: malformed assignment {part} - expected: <channels>,<port>,<attenuation>")
            except Exception as e:
                print(f"Error in slot {part}: {e}")
