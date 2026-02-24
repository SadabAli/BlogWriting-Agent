from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Say hello in one short sentence."
)

print("Response:")
print(response.text)