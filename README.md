## w0sa — WSS + OSA Simulator

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` is a Python-based tool to simulate the output of an Optical Spectrum Analyzer (OSA) based on configurable settings of a Wavelength Selective Switch (WSS), without requiring physical OSA.

##### 🎯 Goals

- Emulate realistic OSA output in response to WSS configuration changes
- Provide a Command-Line Interface (CLI)

##### 📁 Project Structure

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

##### 🔧 Installation

```bash
# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -e .

# Launch w0sa
$ w0sa
```
