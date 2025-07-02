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
