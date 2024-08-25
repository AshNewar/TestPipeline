import openai

openai.api_key = 'YOUR_API_KEY'

def evaluate_question_quality(questions, content_summary):
    prompt = f"Evaluate the following questions: {questions}. Content summary: {content_summary}"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def evaluate_relevance(relevant_links, content_summary):
    prompt = f"Evaluate the relevance of these links: {relevant_links}. Content summary: {content_summary}"
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()
