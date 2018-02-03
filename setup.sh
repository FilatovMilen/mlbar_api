#!/usr/bin/env bash

virtualenv lib
source lib/bin/activate
pip3 install -r requirements.txt

./migrate.sh
