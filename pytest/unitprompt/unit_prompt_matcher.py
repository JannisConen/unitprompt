import pytest
from matchers.parsable.test_parsable_json import assert_parsable_json
from pytest.unitprompt.matchers.parsable.test_parsable_csv import assert_parsable_csv
from pytest.unitprompt.matchers.parsable.test_parsable_xml import assert_parsable_xml
from pytest.unitprompt.matchers.parsable.test_parsable_yaml import assert_parsable_yaml

from matchers.uses.test_uses_html import assert_is_html
from matchers.uses.test_uses_latex import assert_is_latex
from matchers.uses.test_uses_markdown import assert_is_markdown

from matchers.style.test_conciseness import assert_concise_answer, assert_conciseness

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

@pytest.fixture
def uses_html():
    return assert_is_html

@pytest.fixture
def uses_markdown():
    return assert_is_markdown

@pytest.fixture
def uses_latex():
    return assert_is_latex

@pytest.fixture
def is_concise():
    return assert_conciseness

@pytest.fixture
def is_concise_answer():
    return assert_concise_answer
