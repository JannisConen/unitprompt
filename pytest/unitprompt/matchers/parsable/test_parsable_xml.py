import xml.etree.ElementTree as ET
import pytest

def assert_parsable_xml(received: str):
    try:
        ET.fromstring(received)
    except ET.ParseError:
        pytest.fail(f"Expected {received} to be parsable XML")