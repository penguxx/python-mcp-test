from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
YOUR_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=YOUR_API_KEY)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)