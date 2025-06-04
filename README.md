# Antibody Numbering Web Interface

This repository contains a minimal Flask application that wraps the
[ANARCI](https://github.com/oxpig/ANARCI) library. Users can paste an
antibody sequence into the web form and retrieve the numbered sequence
using their choice of numbering scheme.

## Setup

1. Install the dependencies. ANARCI is installed from GitHub:
   ```bash
   pip install -r requirements.txt
   ```
   ANARCI itself requires `hmmer` to be available on your system.
   Please follow the installation instructions from the ANARCI
   repository if numbering fails.

2. Run the development server:
   ```bash
   python app.py
   ```

3. Open a browser at <http://localhost:5000> and submit a sequence to
   see the numbering result.
