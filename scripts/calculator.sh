#!/bin/sh
#
#
# Author : Anand Nevase <anand.nevase@xoriant.com>
#
# Description: Script for running or installing TechX calculator application in docker.
# This script fetches deploy.properties to get EGG File
#
# Usage:
#   To install calculator application from egg, run following command
#           $ sh calculator.sh install 
#   To run calculator application inside docker container, run following command
#           $ sh calculator.sh run


# source deploy properties 
source /calculator/techx_calculator.deploy.properties

# function to install calculator application from python egg file
install_calculator(){
    easy_install-2.7 /calculator/${TECHX_CALCULATOR_EGG_FILE}
}
# function to run xporter application
run_calculator_application(){
    HTTP_LOG_DIR=$(python -c 'from techx.calculator import config; print config.logs_dir')
    mkdir -p $HTTP_LOG_DIR
    LOG_FILE="server.log"
    calculator 2>&1 | tee -a $HTTP_LOG_DIR/$LOG_FILE
}

if [ "$1" = "run" ]
then
    # call run_calculator_application function to run calculator app
    run_calculator_application
elif [ "$1" = "install" ]
then
    # call install_calculator function to install calculator app
    install_calculator
else
    echo "run/install argument missing"
fi

