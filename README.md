## w0sa — WSS + OSA Simulator

[📘 English](README.md) | [📗 Español](README.es.md)

`w0sa` is a Python-based tool to simulate the output of an Optical Spectrum Analyzer (OSA) based on configurable settings of a Wavelength Selective Switch (WSS), without requiring physical OSA.

##### 🎯 Goals

- Emulate realistic OSA output in response to WSS configuration changes
- Provide both a Command-Line Interface (CLI)

##### 📁 Project Structure

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

- `OSA_SHOW [-wv | -freq | -save]` — Plot the optical spectrum (in wavelength or frequency)

- `SETP <P#> -> <spectrum_id>` — Set input spectrum for a port (in dBm)

- `DCC <ch>=<start_slot>:<end_slot>; ...` — Define channel slot plans

- `DCCS` — Show current channel-slot mappings

- `URA <ch>,<port>,<attenuation>; ...` — Route a port to a channel and apply attenuation

- `URAS` — Show current channel-port mappings

- `RSW` — Update the WSS with the reconfigured channel plan

- `DCCG` — Generate a default DCC command

- `URAG <spectrum_id>` — Generate a URA command from an output spectrum
