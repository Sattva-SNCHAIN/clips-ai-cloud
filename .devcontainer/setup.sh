#!/bin/bash
set -e

echo "Installing system dependencies..."
sudo apt update
sudo apt install -y ffmpeg libmagic1 python3-venv

echo "Creating virtual environments..."

# environment: clipsai
python3 -m venv /workspaces/env-clipsai
source /workspaces/env-clipsai/bin/activate
pip install --upgrade pip
pip install clipsai

deactivate

# environment: whisperx
python3 -m venv /workspaces/env-whisperx
source /workspaces/env-whisperx/bin/activate
pip install --upgrade pip
pip install "whisperx @ git+https://github.com/m-bain/whisperx.git"

deactivate

echo "All environments installed!"
