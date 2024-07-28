import pytest
from matchers.parsable.test_parsable_json import assert_parsable_json
from pytest.unitprompt.matchers.parsable.test_parsable_csv import assert_parsable_csv
from pytest.unitprompt.matchers.parsable.test_parsable_xml import assert_parsable_xml
from pytest.unitprompt.matchers.parsable.test_parsable_yaml import assert_parsable_yaml

@pytest.fixture
def parsable_json():
    return assert_parsable_json

@pytest.fixture
def parsable_yaml():
    return assert_parsable_yaml

@pytest.fixture
def parsable_xml():
    return assert_parsable_xml

@pytest.fixture
def parsable_csv():
    return assert_parsable_csv