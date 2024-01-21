# Project Setup for Jupyter Notebook

This repository contains scripts to set up a project structure with directories for each chapter and a virtual environment for running Jupyter Notebooks. The provided scripts are for PowerShell, and they automate the process of creating directories and setting up a virtual environment.

## Steps to Set Up the Project

### 1. Create Directories

Run the following command to create directories for each chapter:

```bash
mkdir Chapter01 Chapter02 Chapter03 Chapter04
```

### 2. Create Virtual Environment

Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

### 3. Activate Virtual Environment and Install Packages

The PowerShell script checks if the virtual environment exists before activating and installing the required packages. Run the following script in PowerShell:

```powershell
if (Test-Path .\venv) {
    # Activate virtual environment
    .\venv\Scripts\Activate.ps1

    # Install Jupyter Notebook inside the virtual environment
    pip install notebook

    # Upgrade pip inside the virtual environment
    python -m pip install --upgrade pip

    # Launch Jupyter Notebook
    jupyter notebook
} else {
    Write-Host "Error: Virtual environment not found. Please ensure 'python -m venv' is successful."
}
```

This script activates the virtual environment, installs Jupyter Notebook, upgrades pip, and launches Jupyter Notebook.

## Note

Ensure that you have Python and PowerShell installed on your system before running the provided scripts. If there are any issues, check the error messages and make sure that the virtual environment is created successfully using the `python -m venv` command.

Feel free to customize the project structure and scripts according to your requirements.