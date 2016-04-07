# Copyright (c) 2015 Nutanix Inc. All rights reserved.
#
# Author: Anand Nevase
#
# Setup TechX Calculator Development environment for Python
#
# NOTE: This should be run by `source setup-dev-env`


echo "---------------------------------------------------"
echo "| Setting up TechX Calculator development environment. |"
echo "---------------------------------------------------"

if (python -c 'import sys; print sys.real_prefix' &>/dev/null); then
    echo
    echo "Virtualenv is already activated."
    echo
elif ! $(python -c "import virtualenv" &> /dev/null); then
    echo
    echo "No virtualenv package found. Please run 'pip install virtualenv' first."
    echo
    return
fi

if [ ! -d "calculator-dev" ]; then
    echo "Creating a new virtual environment for Python."
    virtualenv calculator-dev

    echo "Activating the virtual environment."
    source calculator-dev/bin/activate

    echo "Installing all dependencies"
    pip install -r requirements.txt

    echo "Registering TechX Calculator package in the virtualenv."
    python setup.py develop
else
    echo "Activating the virtual environment."
    source calculator-dev/bin/activate
fi

export TECHX_CALCULATOR_AUTO_RELOAD=on
export TECHX_CALCULATOR_ENV="DEV"

echo
echo "NOTE: Make sure the virtualenv is activated. You should see the text (calculator-dev) in the prompt."
echo