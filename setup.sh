#!/usr/bin/bash

# Clearing the screen.
clear

# Check if the .venv directory exists, then remove it if it does.
if [ -d "$(pwd)/.venv" ]; then
    # Removing the current .venv directory
    rm -rf "$(pwd)/.venv"
fi

# Creating a new Python virtual environment.
python3 -m venv .venv --prompt venv

# Activating the Python virtual environment.
# shellcheck disable=SC1091
source ./.venv/bin/activate

# Upgrading pip to the latest version.
pip install --upgrade pip

# Installing the required packages from the requirements.txt file.
pip install -r requirements.txt

# Indicating that a new Python virtual environment has been created.
echo "A new python virtual environment has been successfully created."
