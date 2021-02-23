#!/bin/bash
# (C) 2020-2021 Keir Finlow-Bates
# See LICENSE for the licensing details of this software

if [ -z $BASH_VERSION ] ; then
	echo "You must run this script using bash" 1>&2
	exit 1
fi

# uncomment for debug info
set -x

# This script uses python3, so we need to
# activate the virtual python3 environment
export PATH="/home/$USER/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Here we run Flask, and it works!
FLASK_APP=flask-app.py flask run --port 5050
