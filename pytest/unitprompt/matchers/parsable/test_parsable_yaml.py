import yaml
import pytest

def assert_parsable_yaml(value):
    try:
        yaml.safe_load(value)
    except yaml.YAMLError:
        pytest.fail(f"Expected {value} to be parsable YAML")