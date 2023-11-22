#!/bin/zsh
# This script will setup the respective dataset to be analyzed 

python3 ver_cli.py create_sources_file quickstart
python3 ver_cli.py add_csv quickstart quickstart quickstart_datasets/$1/
python3 ver_cli.py profile quickstart output_profiles_json
python3 ver_cli.py build_dindex output_profiles_json/ --force
echo "setup complete. run 'python3 ver_quick_start.py' to generate views. \n 
    Be sure to change the `data_path` variable and specify a relevant example query."