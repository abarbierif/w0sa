## w0sa — Simulador de WSS + OSA

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` es una herramienta basada en Python para simular la salida de un Analizador de Espectro Óptico (OSA) según la configuración de un Switch Selectivo en Longitud de Onda (WSS), sin necesidad de un OSA físico.

##### 🎯 Objetivos

- Emular de forma realista la salida de un OSA ante cambios en la configuración del WSS
- Proveer una interfaz de línea de comandos (CLI)

##### 📁 Estructura del Proyecto

```bash
.
├── calibration
├── cli
├── core
├── data
├── README.es.md
├── README.md
├── requirements.txt
├── utils
└── w0sa.py
```

##### 🔧 Instalación

```bash
# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

# Launch w0sa
$ python3 w0sa.py
```
