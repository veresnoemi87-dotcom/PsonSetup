#!/bin/bash

echo "========================="
echo "Installing pson (Unix)"
echo "========================="

# Check Python
if ! command -v python3 &> /dev/null
then
    echo "ERROR: python3 is not installed."
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install package
echo "Installing pson..."
python3 -m pip install .

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Installation failed."
else
    echo ""
    echo "✅ pson installed successfully!"
    echo "Try: pson -v"
fi