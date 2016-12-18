#!/usr/bin/env bash

pip install virtualenv
virtualenv .
source bin/activate
pip install -r requirements.txt
. run.sh
