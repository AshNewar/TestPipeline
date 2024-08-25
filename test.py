# test_validation.py
import pytest
import json
from validation import validate_json, validate_questions, validate_relevant_links

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def test_json_validation():
    data = load_data('final_output.json')
    assert all(validate_json(entry) for entry in data)

def test_question_length():
    data = load_data('final_output.json')
    assert all(validate_questions(entry['questions']) for entry in data)

def test_relevant_links():
    data = load_data('final_output.json')
    assert all(validate_relevant_links(entry['relevant_links']) for entry in data)
