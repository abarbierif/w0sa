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
    """
    W0SAShell class is intended to simulate real WSS interaction.
    """

    intro = """
                       ______                        
                      /      \                       
         __   __   __|  _____ \ _______  ______  
        |  \ |  \ |  | /     \|/       \|      \   
        |  | |  | |  | |     ||  ______| \_____ |
        |  | |  | |  | |     ||\ |_____  ______||
        |  |_/  |_/  | \_____/|_\_____ || _____ |
         \           |\       |        |\ \____||
          \____|\____| \_____/ \______/  \______|
    
    Welcome to w0sa CLI. Type help or ? to list commands.
    """
    prompt = "w0sa> "


    def __init__(self):
        super().__init__()
        self.wss = WSSimulator()
        self.osa = OSAmulator()
    
    def do_exit(self, arg):
        """
        ES: Sale de la interfaz de línea de comandos de w0sa.\n
        EN: Exits the w0sa CLI.
        """
        print("Exiting w0sa...")
        return True

    def do_clear(self, arg):
        """
        ES: Limpia la pantalla del terminal.\n
        EN: Clears the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_ls_spectrums(self, arg):
        """
        ES: Lista los espectros disponibles.\n
        EN: Lists the available spectrums.

        Example
        -------
        >>> ls_spectrums
        """
        for spectrum in INPUT_SPECTRUMS.keys():
            print(f"{spectrum} -> {SPECTRUM_DESCRIPTION[spectrum]}")

    def do_ls_ports(self, arg):
        """
        ES: Lista la configuración actual de puertos.\n
        EN: Lists current ports configuration.

        Example
        -------
        >>> ls_ports
        """
        
        for port, port_config in self.wss.ports.items():
            print(f"{port} -> {port_config['spectrum_id']}")

    def do_OSA_SHOW(self, arg):
        """
        ES: Muestra el espectro óptico medido por el OSA (Analizador de Espectro Óptico) simulado.\n
        EN: Displays the optical spectrum measured by the wssulated OSA (Optical Spectrum Analyzer).

        Examples
        --------
        >>> OSA_SHOW
        >>> OSA_SHOW -wv #default
        >>> OSA_SHOW -fq
        >>> OSA_SHOW -save
        """
        
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
        """
        ES: Define la resolución de entrada.\n
        EN: Sets input resolution.

        Examples
        --------
        >>> SINRES 1.0 #default
        >>> SINRES 0.03
        """

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
        """
        ES: Define la resolución de salida.\n
        EN: Sets output resolution.

        Examples
        --------
        >>> SOUTRES 1.0 #default
        >>> SOUTRES 0.2
        """

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
        """
        ES: Define el span del OSA.\n
        EN: Sets OSA span.

        Examples
        --------
        >>> SSPAN 50.0 #default
        >>> SSPAN 35.0
        """

        if not arg.strip():
            print("Error: no assignments provided")
            return

        self.osa.spanning(span=float(arg))

    def do_SETP(self, arg):
        """
        ES: Define el espectro de entrada (en dBm) de un puerto del WSS.\n
        EN: Sets the input spectrum (in dBm) of a WSS input port.

        Examples
        --------
        >>> SETP P2 -> EDFA1000_r1.0_s50 #default
        >>> SETP P9 -> EDFA1000_r0.03_s50 #Maximum port (P1-P9)
        """
        
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
        """
        ES: Define los rangos de slots para cada canal lógico en el WSS.\n
        EN: Defines slot ranges for each logical channel in the WSS.

        Examples
        --------
        >>> DCC 1=90:93; 2=94:94
        >>> DCC 1=1:8;2=9:16;3=17:24;4=25:32;5=33:40;6=41:48;7=49:56;8=57:64;9=65:72;10=73:80;11=81:90;12=91:96;13=97:104;14=105:112;15=113:120;16=121:128;17=129:136;18=137:144;19=145:152;20=153:160;21=161:168;22=169:176;23=177:184;24=185:192;25=193:200;26=201:208;27=209:216;28=217:221;29=222:232;30=233:240;31=241:248;32=249:256;33=257:264;34=265:272;35=273:280;36=281:290;37=291:296;38=297:304;39=305:312;40=313:320;41=321:328;42=329:336;43=337:344;44=345:352;45=353:360;46=361:368;47=369:376;48=377:384
        """

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
        """
        ES: Muestra el estado actual de la configuración de canales.\n
        EN: Displays the current channel configuration status.

        Example
        -------
        >>> DCCS
        """
        
        status = ''
        for ch,ch_config in self.wss.channels.items():
            status += str(ch) + '=' + str(ch_config['sli']) + ':' + str(ch_config['slf']) + ';'

        print(status[:-1])

    def do_URA(self, arg):
        """
        ES: Asocia un puerto de entrada a un canal lógico y aplica una atenuación en dB.\n
        EN: Assigns an input port to a logical channel and applies attenuation in dB.

        Examples
        --------
        >>> URA 1,1,0.0; 2,1,20.0
        >>> URA 1,2,14.0;2,2,14.0;3,2,15.0;4,2,16.0;5,2,16.0;6,2,17.0;7,2,17.0;8,2,17.0;9,2,17.0;10,2,18.0;11,2,18.0;12,2,0.0;13,2,0.0;14,2,0.0;15,2,0.0;16,2,0.0;17,2,0.0;18,2,0.0;19,2,0.0;20,2,0.0;21,2,0.0;22,2,0.0;23,2,0.0;24,2,0.0;25,2,0.0;26,2,0.0;27,2,0.0;28,2,0.0;29,2,20.0;30,2,20.0;31,2,20.0;32,2,20.0;33,2,20.0;34,2,20.0;35,2,20.0;36,2,20.0;37,2,3.0;38,2,6.0;39,2,8.0;40,2,11.0;41,2,14.0;42,2,16.0;43,2,16.0;44,2,16.0;45,2,16.0;46,2,15.0;47,2,13.0;48,2,12.0
        """

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
        """
        ES: Actualiza el WSS con el plan de canales reconfigurado.\n
        EN: Updates the WSS with the reconfigured channel plan.

        Example
        -------
        >>> RSW
        """
        
        self.wss.channels_status = copy.deepcopy(self.wss.channels)
        self.wss.spectrum = {}
        self.wss.get_spectrum()

    def do_URAS(self, arg):
        """
        ES: Muestra el estado actual de la configuración de canales.\n
        EN: Displays the current channel configuration status.

        Example
        -------
        >>> URAS
        """

        status = ''
        for ch,ch_config in self.wss.channels_status.items():
            status += str(ch) + ',' + (str(ch_config['prt'])[1:] if ch_config['prt'] is not None else str(ch_config['prt'])) + ',' + str(ch_config['atn']) + ';'

        print(status[:-1])

    def do_DCCG(self, arg):
        """
        ES: Genera un comando DCC por defecto.\n
        EN: Generates a default DCC command.

        Example
        -------
        >>> DCCG
        """
        
        self.wss.get_dcc()

    def do_URAG(self, arg):
        """
        ES: Genera un comando URA desde un espectro de salida.\n
        EN: Generates an URA command from an output spectrum.

        Example
        -------
        >>> URAG DWDM_r1.0_s50
        """

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
        """
        ES: Convierte de mW a dB.\n
        EN: Converts mW to dB.

        Example
        -------
        >>> 2dB 371.3
        """

        if not arg.strip():
            print("Error: no assignments provided")
            return

        mw = float(arg)

        print(mW2dBm(mw=mw), 'dB')


    def do_dB2(self, arg):
        """
        ES: Convierte de dB a mW.\n
        EN: Converts dBm to mW.

        Example
        -------
        >>> dB2 3.0
        """

        if not arg.strip():
            print("Error: no assignments provided")
            return

        dbm = float(arg)

        print(dBm2mW(dbm=dbm))
