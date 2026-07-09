import google.generativeai as genai

# Configure Gemini using your API key
genai.configure(api_key="Api key")

# Choose the AI model
model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_answer(question):
    """
    Takes a question as input.
    Sends it to Gemini.
    Returns the AI's answer.
    """
    
    response = model.generate_content(question)

    return response.text
