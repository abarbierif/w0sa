## w0sa — Simulador de WSS + OSA

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` es una herramienta basada en Python para simular la salida de un Analizador de Espectro Óptico (OSA) según la configuración de un Switch Selectivo en Longitud de Onda (WSS), sin necesidad de un OSA físico.

##### 🎯 Objetivos

- Emular de forma realista la salida de un OSA ante cambios en la configuración del WSS
- Proveer tanto una interfaz de línea de comandos (CLI)

##### 📁 Estructura del Proyecto

```bash
.
├── pyproject.toml
├── README.md
├── README.es.md
├── requirements.txt
├── tests
└── w0sa
    ├── cli
    ├── core
    ├── data
    └── gui
```

##### 🔧 Instalación (en desarrollo...)

```bash
# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install the project in editable mode
$ pip install -e .
```

##### 🧑‍💻 Uso

```bash
# Launch de CLI
$ w0sa
```

##### Comandos Soportados

- `exit` — Salir de la terminal

- `clear` — Limpiar la terminal

- `OSA_SHOW [-wv | -freq | -save]` — Mostrar el espectro óptico (en longitud de onda o frecuencia)

- `SETP <P#> -> <spectrum_id>` — Asociar un espectro de entrada a un puerto (in dBm)

- `DCC <ch>=<start_slot>:<end_slot>; ...` — Definir el plan de canales

- `DCCS` — Mostrar el mapeo canal-slot actual

- `URA <ch>,<port>,<attenuation>; ...` — Rutear un puerto a un canal y aplicar atenuación
  
- `URAS` — Mostrar el mapeo canal-puerto actual

- `RSW` — Actualizar el WSS con el plan de canales reconfigurado

- `DCCG` — Generar un comando DCC por defecto

- `URAG <spectrum_id>` — Generar un comando URA desde un spectro de salida
