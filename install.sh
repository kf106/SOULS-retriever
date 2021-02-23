#!/bin/bash
# (C) 2020-2021 Keir Finlow-Bates
# See LICENSE for the licensing details of this software

# Uncomment for debugging
#set -x

# Check that the correct shell is used.
if [ -z $BASH_VERSION ] ; then
	echo -e "You must run this script using bash." 1>&2
	exit 1
fi

# Make sure we are running as sudo.
if [[ $EUID -ne 0 ]]; then
	echo -e "This script must be run using sudo." 1>&2
	exit 1
fi

# Check we are not running as root, as that messes
# up the pyenv install (root's home is in /root, whereas
# users are in /home/$USER, and this results in the
# wrong path for pyenv.

if [[ "$SUDO_USER" == "root" ]]; then
	echo -e "This script must be not be run as root." 1>&2
	exit 1
fi

if [[ "$SUDO_USER" == "" ]]; then
	echo -e "This script must be not be run as root." 1>&2
	exit 1
fi

### Sudo installation section

# this installs the required packages for the pyenv system
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev\
  libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl\
  git curl

# This calls the pyenv installation script as the local user.
# I would prefer to include it in this script, but none of the tricks
# I know for dropping back to the ordinary user seem to work.
su $SUDO_USER -c "./pyenv.sh"



