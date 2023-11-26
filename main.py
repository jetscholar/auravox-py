from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables as before
api_key = os.getenv('OPENAI_KEY')

# Set your OpenAI API key
openai.api_key = api_key

def get_openai_response(prompt):
    """
    Get a response from OpenAI's API given a prompt.
    """
    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo",  # You can experiment with different models
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    return response['choices'][0]['message']['content'].strip()

def main():
    print("Chatbot: Hello! I'm your virtual assistant. Ask me anything or give me a command.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Get OpenAI's response
        bot_response = get_openai_response(user_input)

        print(f"Chatbot: {bot_response}")

if __name__ == "__main__":
    main()
