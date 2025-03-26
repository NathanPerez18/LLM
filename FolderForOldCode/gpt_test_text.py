import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI client
client = OpenAI(api_key=api_key)

def analyze_text_with_gpt(user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Does the following message look like a scam or phishing attempt? Be specific in your analysis.\n\nMessage: {user_text}"
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    test_message = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim now!"
    print("📨 Sending test text to GPT-4o-mini...\n")
    result = analyze_text_with_gpt(test_message)
    print("🧠 GPT-4 Response:\n")
    print(result)
