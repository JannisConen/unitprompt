import csv
import io
import pytest

def assert_parsable_csv(received: str):
    try:
        reader = csv.reader(io.StringIO(received))
        for row in reader:
            pass  # Just iterate over rows to check for parse errors
    except csv.Error:
        pytest.fail(f"Expected {received} to be parsable CSV")