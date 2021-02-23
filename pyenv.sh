#!/bin/bash
# (C) 2020-2021 Keir Finlow-Bates
# See LICENSE for the licensing details of this software

# We install pyenv as the local user so it ends up in 
# the proper home directory

curl https://pyenv.run | bash

export PATH="/home/$USER/.pyenv/bin:$PATH"
eval "$(/home/$USER/.pyenv/bin/pyenv init -)"
eval "$(/home/$USER/.pyenv/bin/pyenv virtualenv-init -)"

# Get python 3.8.2 and create the local environment
pyenv install 3.8.2
pyenv virtualenv 3.8.2 myenv
pyenv local myenv

# Which is why this will show version 3.8.2
python --version

# We need the wheel package first
pip install wheel

# Installs all the packages needed for the project to the pyenv
pip install --upgrade -r requirements.txt

# When your project is complete use
# $ pip freeze > requirements.txt
# to make sure the requirements are up to date and the right packages are installed

# To upgrade all pip packages run
# $ pip freeze |sed -ne 's/==.*//p' |xargs pip install -U --
