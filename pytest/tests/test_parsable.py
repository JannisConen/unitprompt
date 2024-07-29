import pytest
from unitprompt.matchers.parsable.test_parsable_json import assert_parsable_json
from unitprompt.matchers.parsable.test_parsable_yaml import assert_parsable_yaml
from unitprompt.matchers.parsable.test_parsable_xml import assert_parsable_xml
from unitprompt.matchers.parsable.test_parsable_csv import assert_parsable_csv

def test_json_parsable():
    json_string = '{"key": "value"}'
    assert_parsable_json(json_string)    
    
def test_json_parsable_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_parsable_json('{"key": "value"')
        
def test_parsable_yaml():
    yaml_string = 'key: value'
    assert_parsable_yaml(yaml_string)

def test_parsable_yaml_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_parsable_yaml('key: value\nanother_key another_value')
        
def test_parsable_xml():
    xml_string = '<root><key>value</key></root>'
    assert_parsable_xml(xml_string)
    
def test_parsable_xml_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_parsable_xml('<root><key>value</key></root')
        
def test_parsable_csv():
    csv_string = 'key,value\n1,2\n3,4'
    assert_parsable_csv(csv_string)
    
def test_parsable_csv_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_parsable_csv('name,age\nJohn,30\nDoe')