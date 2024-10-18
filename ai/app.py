import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def simple_ai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Example usage
user_input = input("Ask me anything: ")
ai_response = simple_ai(user_input)
print("AI says:", ai_response)

