# 🧪 w0sa — WSS + OSA Simulator

`w0sa` is a Python-based tool to simulate the output of an Optical Spectrum Analyzer (OSA) based on configurable settings of a Wavelength Selective Switch (WSS), without requiring physical OSA.

---

## 🎯 Goals

- Emulate realistic OSA output in response to WSS configuration changes
- Provide both a Command-Line Interface (CLI) and a GUI

---

## 📁 Project Structure

w0sa/
├── w0sa/ 			# Main package
│ ├── cli/ 			# CLI interface (cmd.Cmd-based)
│ ├── gui/ 			# GUI viewer using pyqtgraph
│ ├── core/ 		# Core simulation logic (WSS, channels, spectrum)
│ ├── config/ 		# YAML configs, profiles
│ └── utils/ 		# Helper functions, logging
├── tests/ 			# Unit tests (pytest)
├── README.md 		# You're here!
├── pyproject.toml 	# Project metadata and entry points
├── .gitignore 		# Files to exclude from version control

## 🚀 Installation

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the project in editable mode
pip install -e .
```

## 🧑‍💻 Usage

- Launch de CLI

```bash
w0sa
```