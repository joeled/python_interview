brew install pyenv
pyenv install 3.9.0
pyenv global 3.9.0
pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install pytest