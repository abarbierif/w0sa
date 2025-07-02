from w0sa.core.wss_simulator import WSSimulator
from w0sa.core.osa_simulator import OSAmulator
from w0sa.data.config_spectrums import INPUT_SPECTRUMS, OUTPUT_SPECTRUMS, SPECTRUM_DESCRIPTION
from w0sa.utils.conversions import *
import cmd
import numpy as np
import matplotlib.pyplot as plt
import os
import copy

class W0SAShell(cmd.Cmd):
    intro = "Welcome to w0sa CLI. Type help or ? to list commands."
    prompt = "w0sa> "


    def __init__(self):
        super().__init__()
        self.wss = WSSimulator()
        self.osa = OSAmulator()
    
    def do_exit(self, arg):
        """EN: Exits the w0sa CLI.\nES: Sale de la interfaz de línea de comandos de w0sa.\n\n Example:\n > exit"""
        print("Exiting w0sa...")
        return True

    def do_clear(self, arg):
        """EN: Clears the terminal screen.\nES: Limpia la pantalla del terminal.\n\n Example:\n > clear"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_ls_spectrums(self, arg):
        """EN: Lists the available spectrums.\nES: Lista los espectros disponibles.\n\n Example:\n > ls_spectrums"""
        for spectrum in INPUT_SPECTRUMS.keys():
            print(f"{spectrum} -> {SPECTRUM_DESCRIPTION[spectrum]}")

    def do_ls_ports(self, arg):
        """EN: Lists current ports configuration.\nES: Lista la configuración actual de puertos.\n\n EXAMPLE:\n > ls_ports"""
        for port, port_config in self.wss.ports.items():
            print(f"{port} -> {port_config['spectrum_id']}")

    def do_OSA_SHOW(self, arg):
        """EN: Displays the optical spectrum measured by the wssulated OSA (Optical Spectrum Analyzer).\nES: Muestra el espectro óptico medido por el OSA (Analizador de Espectro Óptico) wssulado.\n\n - Syntax: OSA_SHOW [-wv | -freq]\n - -wv: Plot in wavelength (nm) [default]\n - -fq: Plot in frequency (THz)\n - -save: Save spectrum as csv\n\n Example:\n > OSA_SHOW\n > OSA_SHOW -fq"""
        
        C = 299792458 # light speed m/s

        flags = set(arg.strip().split())

        if not flags.issubset({'-wv','-fq','-save'}):
            print("Error: invalid option(s)")
            return
        
        freq = None
        if '-fq' in flags:
            freq = True
        else:
            freq = False
        
        if '-save' in flags:
            save = True
        else:
            save = False
        
        wss_spectrum = self.wss.spectrum
        self.osa.show(data=wss_spectrum, freq=freq, save=save)

    def do_SINRES(self, arg):
        """EN: Sets input resolution.\nES: Define la resolución de entrada.\n\n - Syntax: SINRES <resolution>\n Input resolution must match with resolution of input spectrum to calculate correct attenuation values."""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        valid_resolutions = ['1.0', '0.5', '0.2', '0.1', '0.07', '0.05', '0.03']

        if not arg in valid_resolutions:
            print("Error: Invalid resolution. Valid resolutions are: 1.0, 0.5, 0.2, 0.1, 0.07, 0.05 and 0.03 (nm)")
            return

        self.osa.set_inres(inres=float(arg))
        print(f"input resolution set to {arg}")

    def do_SOUTRES(self, arg):
        """EN: Sets output resolution.\nES: Define la resolución de salida.\n\n - Syntax: SOUTRES <resolution>\n"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        valid_resolutions = ['1.0', '0.5', '0.2', '0.1', '0.07', '0.05', '0.03']

        if not arg in valid_resolutions:
            print("Error: Invalid resolution. Valid resolutions are: 1.0, 0.5, 0.2, 0.1, 0.07, 0.05 and 0.03 (nm)")
            return
        
        self.osa.set_outres(outres=float(arg))
        print(f"output resolution set to {arg}")

    def do_SSPAN(self, arg):
        """EN: Sets OSA span.\nES: Define el span del OSA.\n\n - Syntax: SSPAN <span>\n"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        self.osa.spanning(span=float(arg))

    def do_SETP(self, arg):
        """EN: Sets the input spectrum (in dBm) of a WSS input port.\nES: Define el espectro de entrada (en dBm) de un puerto del WSS.\n\n - Syntax: set_port <port> -> <spectrum_id>\n - Ports: P1–P9\n - Type "ls_ports" to list available spectra (IDs)\n\n Example:\n > SETP P1 -> default\n > SETP P2 -> default"""
        
        if not arg.strip():
            print("Error: no assignments provided")
            return

        try:
            prt, sid = arg.split('->', 1)
            prt = prt.strip()
            sid = sid.strip()

            if prt not in self.wss.ports.keys():
                print(f"Error: invalid port {prt}. Valid ports: P1-P9.")
                return

            if sid not in INPUT_SPECTRUMS.keys():
                print(f"Error: invalid spectrum key {sid}. Use <lss> to list available spectra.")
                return

            self.wss.prt_pwr_set(prt=prt, sid=sid)

        except ValueError:
            print(f"Error: malformed assignment {arg} - expected: <port> -> <spectrum_id>.")
        except Exception as e:
            print(f"Unexpected error set_port {e}.")

    def do_DCC(self, arg):
        """EN: Defines slot ranges for each logical channel in the WSS.\nES: Define los rangos de slots para cada canal lógico en el WSS.\n\n - Syntax: <channel>=<start_slot>:<end_slot>; ...\n - Slot range: 1 to 386 (represents 386 12.5 GHz slots in C-band)\n - Channels can be assigned non-overlapping slot ranges\n\n Example:\n > DCC 1=90:93; 2=94:94\n > DCC 3=100:110"""

        if not arg.strip():
            print("Error: no assignments provided")
            return
        self.wss.channels = {}
        parts = [_.strip() for _ in arg.split(';') if _.strip()]
        for part in parts:
            try:
                ch, sl = part.split('=', 1)
                ch = int(ch)
                sli, slf = sl.split(':', 1)
                sli = int(sli)
                slf = int(slf)
                
                self.wss.dcc_set(ch=ch, sli=sli, slf=slf)

            except ValueError:
                print(f"Error: malformed assignment {part} - expected: <channel>=<slot_i>:<slot_f>")
            except Exception as e:
                print(f"Error in slot {part}: {e}")

    def do_DCCS(self, arg):
        """EN: Displays the current channel configuration status.\nES: Muestra el estado actual de la configuración de canales.\n\n - Syntax: DCCS\n - Shows channel-slot mapping as <channel>=<start_slot>:<end_slot>\n\n Example:\n > DCCS\n 1=90:93; 2=94:94"""
        
        status = ''
        for ch,ch_config in self.wss.channels.items():
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
                
                self.wss.ura_set(ch=ch, prt=prt, atn=atn)

            except ValueError:
                print(f"Error: malformed assignment {part} - expected: <channels>,<port>,<attenuation>")
            except Exception as e:
                print(f"Error in slot {part}: {e}")

    def do_RSW(self, arg):
        """EN: Updates the WSS with the reconfigured channel plan.\nES: Actualiza el WSS con el plan de canales reconfigurado.\n\nExample: > RSW"""
        
        self.wss.channels_status = copy.deepcopy(self.wss.channels)
        self.wss.spectrum = {}
        self.wss.get_spectrum()

    def do_URAS(self, arg):
        """EN: Displays the current channel configuration status.\nES: Muestra el estado actual de la configuración de canales.\n\n - Syntax: URAS\n - Shows channel-slot mapping as <channel>,<port>,<attenuation>\n\n Example:\n > URAS\n 1,1,0.0;2,1,20.0"""

        status = ''
        for ch,ch_config in self.wss.channels_status.items():
            status += str(ch) + ',' + (str(ch_config['prt'])[1:] if ch_config['prt'] is not None else str(ch_config['prt'])) + ',' + str(ch_config['atn']) + ';'

        print(status[:-1])

    def do_DCCG(self, arg):
        """EN: Generates a default DCC command.\mES: Genera un comando DCC por defecto.\n\n - Syntax: DCCG\n - 386 channels\n - 1 slot each channel\n\n Example:\n > DCCG"""
        
        self.wss.get_dcc()

    def do_URAG(self, arg):
        """EN:Generates an URA command from an output spectrum.\nES: Genera un comando URA desde un espectro de salida.\n\n - Syntax: URAG <spectrum_id>\n\n Example:\n > URAG DWDM"""

        if all(self.wss.ports[p]['spectrum'] is None for p in self.wss.ports.keys()):
            print("Error: No ports assigned")
            return
        
        spectrum_id = arg.strip()
        valid_ids = set(OUTPUT_SPECTRUMS.keys())
        if spectrum_id not in valid_ids:
            print("Error: invalid spectrum id")
            return

        self.wss.get_ura(spectrum_id=spectrum_id)

    def do_2dB(self, arg):
        """Converts mW to dBm.\n\n - Syntax: mW2dBm <mW>"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        mw = float(arg)

        print(mW2dBm(mw=mw), 'dB')


    def do_dB2(self, arg):
        """Converts dBm to mW.\n\n - Syntax: dBm2mW <dBm>"""

        if not arg.strip():
            print("Error: no assignments provided")
            return

        dbm = float(arg)

        print(dBm2mW(dbm=dbm))
    
    #def do_CONV(self, arg):
    #    """Converts abosultes unit to dB or viceversa"""

    #    if not arg.strip():
    #        print("Error: no assignments provided")
    #        return

    #    if 
