import os
import openai

user_prompt = input("What would you like to have the AI draw? ")

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
  prompt=f"{user_prompt}",
  n=2,
  size="512x512"
)

print(response)