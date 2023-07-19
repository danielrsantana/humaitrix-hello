import sys

sys.path.append("functions")

from env_reader import get_dotenv

env = get_dotenv()
name = env.get('USERNAME')

def welcome_message():
  print(f'Hello {name}, what would you like me to do?')
  print(f'1) Welcome Message Only')
  print(f'2) API Key Check')

def hello_name():
  print('Welcome to Python!')

def hello_key():
  key =  env.get("OPENAI_API_KEY")
  print(f'Hello {name}! This is your open API key: {key}')

welcome_message()
command = input()

if command == '1':
  hello_name()
elif command == '2':
  hello_key()
else:
  print(f'Sorry, the option [{command}] is not available at the moment!')