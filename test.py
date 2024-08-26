# test_validation.py
import pytest
import json
from validation import validate_json, validate_questions, validate_relevant_links
from openai import evaluate_question_quality, evaluate_relevance  # Import your functions

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


def test_question_quality():
    data = load_data('final_output.json')
    content_summary = "This is a summary of the content."
    for entry in data:
        questions = entry['questions']
        result = evaluate_question_quality(questions, content_summary)
        print("result", result)
        assert result  # Replace with actual checks

def test_relevance():
    data = load_data('final_output.json')
    content_summary = "This is a summary of the content."
    for entry in data:
        relevant_links = entry['relevant_links']
        result = evaluate_relevance(relevant_links, content_summary)
        print("result", result)
        assert result  # Replace with actual checks
