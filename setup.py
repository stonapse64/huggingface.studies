# setup.py
# This script installs all packages required for the Hugging Face NLP Course
# Except torch...
# TODO find a way to install torch with this script

import subprocess
import sys

list_of_packages = ["jupyter", "jupyterlab", "transformers", "pandas", "gradio"]


def upgrade_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])


# Install or upgrade each package in the list
for package_name in list_of_packages:
    upgrade_package(package_name)

subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--index-url", "https://download.pytorch.org/whl/cu121", "torch"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--index-url", "https://download.pytorch.org/whl/cu121", "torchvision"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--index-url", "https://download.pytorch.org/whl/cu121", "torchaudio"])

