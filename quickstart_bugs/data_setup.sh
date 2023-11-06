#!/bin/zsh
# This script will setup the city dataset to be analyzed 

python3 ver_cli.py create_sources_file quickstart
python3 ver_cli.py add_csv quickstart quickstart quickstart_bugs/$1/
python3 ver_cli.py profile quickstart output_profiles_json
python3 ver_cli.py build_dindex output_profiles_json/ --force