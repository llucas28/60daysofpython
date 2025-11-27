from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
   messages=[
        {
          "role": "user",
          "content": "oi, tudo bem?"

        }
    ],
    model="gpt-4.1"
)

print(chat_completion)