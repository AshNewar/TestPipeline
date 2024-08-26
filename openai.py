import google.generativeai as genai

genai.configure(api_key="AIzaSyC67tV42R8A5-v8r2wMr7mzK7TSLYMQvWM")  # Replace with your actual API key

model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure the model name is correct

def evaluate_question_quality(questions, content_summary):
    prompt = (
        f"Evaluate the quality of these questions based on their clarity, relevance, and conciseness. "
        f"Each question should be clear, relevant to the content summary, and concise (under 80 characters).\n\n"
        f"Questions: {questions}\n\nContent Summary: {content_summary}"
    )
    
    try:
        response = model.generate_content(prompt)
        result = response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        result = "Error in evaluation"
    
    return result

def evaluate_relevance(relevant_links, content_summary):
    prompt = (
        f"Evaluate the relevance of these links based on their connection to the content summary.\n\n"
        f"Links: {relevant_links}\n\nContent Summary: {content_summary}"
    )
    
    try:
        response = model.generate_content(prompt)
        # Assuming response is a dictionary containing 'choices' as a list
        result = response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        result = "Error in evaluation"
    
    return result
