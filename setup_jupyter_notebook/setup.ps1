# Create directories
mkdir Chapter01 Chapter02 Chapter03 Chapter04

# Create virtual environment
python -m venv venv

# Check if venv exists before activating and installing packages
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
