#!/bin/bash

pip --version

INSTALL_DIR="local_lib"
LOG_FILE="install_path.log"


if [ -d "$INSTALL_DIR" ]; then
  echo "Removing existing local_lib folder..." | tee -a $LOG_FILE
  rm -rf "$INSTALL_DIR"
fi

echo "Installing path.py development version..." | tee -a $LOG_FILE
/usr/bin/python3 -m venv $INSTALL_DIR
source $INSTALL_DIR/bin/activate

pip install git+https://github.com/jaraco/path.py@main --target="$INSTALL_DIR" >> $LOG_FILE 2>&1

if [ $? -eq 0 ]; then
  echo "path.py installed successfully." | tee -a $LOG_FILE

  python3 my_program.py
else
  echo "Installation failed. Check the log file for errors." | tee -a $LOG_FILE
fi
