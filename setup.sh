#!/usr/bin/env bash

git clone https://github.com/letmaik/rawpy.git
(cd rawpy;
    pip install -r dev-requirements.txt;
    python setup.py install;
    pip freeze | grep -v rawpy | xargs pip uninstall -y
)
rm -rf rawpy

pip install -r requirements.txt
