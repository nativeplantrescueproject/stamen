# Installation Instructions

## Python virtualenv
For this project, we'll use Python 3.12. The following instructions are primarily for use with `pyenv`, but there's no strict requirement, so long as Python 3.12 is used ultimately.

1. Ensure you have Python 3.12 installed
    - If using `pyenv` for python version management, install 3.12 with `pyenv install 3.12`
    - You may need to add the contents of `pyenv init` to your shell's session scripts (`.bashrc`, `.zshrc`, etc)
    - Then, set 3.12 for your shell session with `pyenv shell 3.12`
2. Referencing Python 3.12, create your virtual environment (venv)
   `python3.12 -m venv /path/to/your/venv/dir/stamen-312`
3. Activate the venv:
   `source /path/to/your/venv/dir/stamen-312/bin/activate`
4. Now install from `requirements.txt` into the venv with:
   `python3.12 -m pip install -r requirements.txt`

   