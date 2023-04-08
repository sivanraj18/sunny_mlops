import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
          config = yaml.safe_load(yaml_file)
    return config
          
def get_data(config_path):
     config = read_params(config_path)
     #print(config)
     df = pd.read_csv(config['data_source']['s3_source'])
     return df


if __name__ == "__main__":

    parse = argparse.ArgumentParser()
    parse.add_argument('--config',default = 'params.yaml')
    args = parse.parse_args()
    get_data(config_path = args.config)

