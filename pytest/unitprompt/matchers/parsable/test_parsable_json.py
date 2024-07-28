import json
import pytest

def assert_parsable_json(received: str):
    try:
        json.loads(received)
    except ValueError:
        pytest.fail(f"Expected {received} to be parsable JSON")