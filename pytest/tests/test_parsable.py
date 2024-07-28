import pytest
from unitprompt.matchers.parsable.test_parsable_json import assert_parsable_json

def test_json_parsable():
    json_string = '{"key": "value"}'
    assert_parsable_json(json_string)