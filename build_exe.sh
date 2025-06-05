#!/usr/bin/env bash
# Build a standalone executable with PyInstaller
set -e
pyinstaller --onefile --add-data "anarci_web/templates:templates" anarci_web/app.py -n anarci-web
