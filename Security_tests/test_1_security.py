from Security_functions.Security_constructions import *
from path.static_paths import *
import yaml

with open(yaml_sec_testdata()) as f:
    data = yaml.safe_load(f)

## SEC data
cmd_name = data["cmd_name"]
cmd_h_key = data["cmd_h_key"]
site_url = data["site_url"]
ssl_key = data["ssl_key"]
tuning_key = data["tuning_key"]
tuning_level_value = data["tuning_level_value"]
cmd_o_key = data["cmd_o_key"]
output_file_url = data['output_file_url']

## Valid data
zero_errors = data['zero_errors']


## Step 1: Start checking site process and check valid result
def test_step1():
    run_process(f'{cmd_name} {cmd_h_key} {site_url} {ssl_key} {tuning_key} {tuning_level_value} {cmd_o_key} {output_file_url}')
    flag = find_phrase_in_file(output_file_url, zero_errors)
    assert flag