# Antibody Numbering Web Interface

This repository contains a minimal Flask application that wraps the
[ANARCI](https://github.com/oxpig/ANARCI) library. Users can paste an
antibody sequence into the web form and retrieve the numbered sequence
using their choice of numbering scheme.

## Installation

You can install the project as a Python package. This installs all
dependencies and provides a command line entry point called
`anarci-web`.

```bash
pip install .
```

If you only want to install the dependencies for development, use:

```bash
pip install -r requirements.txt
```

ANARCI requires `hmmer` to be available on your system. Please follow
the installation instructions from the ANARCI repository if numbering
fails.

## Usage

Run the server after installation with:

```bash
anarci-web
```

Then open a browser at <http://localhost:5000> and submit a sequence to
see the numbering result.

## Building a standalone executable

You can bundle the application and all dependencies into a single
executable using PyInstaller. First install PyInstaller and then run the
provided script:

```bash
pip install pyinstaller
./build_exe.sh
```

The resulting executable will be located in the `dist/` directory.
