#!/usr/bin/env bash

export PROJECT_NAME=stephan-poetschner
#export PYTHON_VERSION=python
export PYTHON_VERSION=python3

## general config ##
# Disabling UI for debconf. (See `man debconf` for more options.)
export DEBIAN_FRONTEND=noninteractive

set -e # Exit script immediately on first error.
set -x # Print commands and their arguments as they are executed.

# set time zone
sudo timedatectl set-timezone 'UTC'

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

sudo locale-gen en_US.UTF-8
sudo DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

cat << EOF >> $HOME/.bashrc

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
EOF

# update package manager resources
sudo apt-get update -y

sudo update-alternatives --set editor /usr/bin/vim.basic

## end general config ##

#### python specifics
sudo apt-get install -y build-essential
sudo apt-get install -y ${PYTHON_VERSION}-setuptools

sudo apt-get install -y ${PYTHON_VERSION} ${PYTHON_VERSION}-dev

sudo apt-get install -y ${PYTHON_VERSION}-pip

# replaced by in future Ubuntu LTS versions?
# ${PYTHON_VERSION} -m ensurepip --user


/usr/bin/${PYTHON_VERSION} -m pip install --user --upgrade pip
/usr/bin/${PYTHON_VERSION} -m pip install --user --upgrade virtualenv

BIN_VIRTUALENV=`find $HOME -name virtualenv -print -quit`

export PROJECT_HOME="/vagrant"
export PROJECT_VENV="${PROJECT_HOME}/venv"
export ACTIVATE_PY="${PROJECT_VENV}/bin/activate"
export ACTIVATE_BIN="source ${PROJECT_VENV}/bin/activate"


    cat <<EOT >> $HOME/.bashrc

HISTSIZE=-1
HISTFILESIZE=-1

source ${ACTIVATE_PY}

EOT

### app-dependancies
if [ ! -f ${ACTIVATE_PY} ]; then
    ${BIN_VIRTUALENV} $PROJECT_VENV --python ${PYTHON_VERSION} --always-copy
fi

