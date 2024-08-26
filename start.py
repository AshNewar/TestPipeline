import pytest
import json

@pytest.fixture
def data():
    # Load data from a file or return a sample data dictionary
    with open('final_output.json', 'r') as file:
        return json.load(file)
