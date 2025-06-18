import argparse
import json
import os
import pandas

from select_habitat import select_habitat

arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--habitat_name', action='store', type=str, required=True, dest='habitat_name')

args = arg_parser.parse_args()
print(args)

habitat_name = args.habitat_name

url = "http://opendap.biodt.eu/ias-pdt/0/outputs/key.csv"
df_hab = pandas.read_csv(url)

habitat_type = habitat_name.replace(' ','_').lower()
selected_hab_abb = str(df_hab[df_hab["hab_name"] == habitat_type]["hab_abb"].values[0])
param_climate_model = 'IPSL-CM6A-LR'
param_species_class = 'Liliopsida'


conf_x =  0.95
conf_y =  0.95
conf_arrow_length = 0.1
print(f"Selected Habitat Abbreviation: {selected_hab_abb}")

habitat_number = select_habitat(selected_hab_abb=selected_hab_abb, habitat_name=habitat_name)



