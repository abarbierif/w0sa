## w0sa — Simulador de WSS + OSA

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` es una herramienta basada en Python para simular la salida de un Analizador de Espectro Óptico (OSA) según la configuración de un Switch Selectivo en Longitud de Onda (WSS), sin necesidad de un OSA físico.

##### 🎯 Objetivos

- Emular de forma realista la salida de un OSA ante cambios en la configuración del WSS
- Proveer tanto una interfaz de línea de comandos (CLI) como una GUI

##### 📁 Estructura del Proyecto

```bash
.
├── pyproject.toml
├── README.md
├── requirements.txt
├── tests
└── w0sa
    ├── cli
    ├── core
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

- `exit` — Salir de la CLI

- `clear` — Limpiar la pantalla de la terminal

- `osa_show [-wv | -freq]` — Mostrar el espectro (`-wv` para longitud de onda, `-freq` para frecuencia)

- `set_prt <port>:<power>` — Definir potencia (dBm) de entrada en un puerto del WSS

- `dcc <ch>=<start_slot>:<end_slot>; ...` — Definir rangos de slots por canal (Plan de Canales)

- `dcc_status` — Ver el mapeo actual de canales a slots

- `ura <ch>,<port>,<attenuation>; ...` — Asociar puertos de entrada a canales con atenuación
