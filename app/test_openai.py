import os
import openai
import sys

sys.path.append("functions")

from env_reader import get_dotenv

env = get_dotenv()
api_key = env.get("OPENAI_API_KEY")
openai.api_key = api_key

print(f'This is my open AI key: {openai.api_key}')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)