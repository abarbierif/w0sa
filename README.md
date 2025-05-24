## 🧪 w0sa — WSS + OSA Simulator

`w0sa` is a Python-based tool to simulate the output of an Optical Spectrum Analyzer (OSA) based on configurable settings of a Wavelength Selective Switch (WSS), without requiring physical OSA.

##### 🎯 Goals

- Emulate realistic OSA output in response to WSS configuration changes
- Provide both a Command-Line Interface (CLI) and a GUI

##### 📁 Project Structure

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

##### 🔧 Deployment

```bash
# Create and activate a virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install the project in editable mode
$ pip install -e .
```

##### 🧑‍💻 Usage

```bash
# Launch de CLI
$ w0sa
```
