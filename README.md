## w0sa — WSS + OSA Simulator

[📘 English](README.md) | [📗 Español](README.es.md)

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

##### 🔧 Installation (in development...)

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

##### Supported CLI Commands

- `exit` — Exit the CLI

- `clear` — Clear the terminal screen

- `osa_show [-wv | -freq]` — Plot the optical spectrum (in wavelength or frequency)

- `set_prt <port>:<power>` — Set input power for a port (in dBm)

- `dcc <ch>=<start_slot>:<end_slot>; ...` — Define channel slot plans

- `dcc_status` — Show current channel-slot mappings

- `ura <ch>,<port>,<attenuation>; ...` — Route a port to a channel and apply attenuation
