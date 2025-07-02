## w0sa — Simulador de WSS + OSA

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` es una herramienta basada en Python para simular la salida de un Analizador de Espectro Óptico (OSA) según la configuración de un Switch Selectivo en Longitud de Onda (WSS), sin necesidad de un OSA físico.

##### 🎯 Objetivos

- Emular de forma realista la salida de un OSA ante cambios en la configuración del WSS
- Proveer una interfaz de línea de comandos (CLI)

##### 📁 Estructura del Proyecto

```bash
.
├── pyproject.toml
├── README.es.md
├── README.md
└── w0sa
    ├── calibration
    ├── cli
    ├── core
    ├── data
    ├── utils
    └── w0sa.py
```

##### 🔧 Instalación

```bash
# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -e .

# Launch w0sa
$ w0sa
```
