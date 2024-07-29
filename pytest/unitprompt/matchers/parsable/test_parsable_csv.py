import csv
import io
import pytest

def assert_parsable_csv(received: str):
    try:
        reader = csv.reader(io.StringIO(received))
        first_row = next(reader)
        num_columns = len(first_row)
        for row in reader:
            if len(row) != num_columns:
                pytest.fail(f"Row length mismatch in CSV: expected {num_columns} columns but found {len(row)} in row {row}")
    except csv.Error as e:
        pytest.fail(f"Expected {received} to be parsable CSV, but error occurred: {e}")