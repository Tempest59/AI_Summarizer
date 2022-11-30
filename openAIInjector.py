import openai
import json

OPENAI_API_KEY = ''

openai.api_key = OPENAI_API_KEY

prompt = "Find a name for a french boy"




def summarizeAi(text, max_tokens):
    prompt = "Write a summary of the following Youtube video script: " + text + " Prompt:"
    response = json.dumps(openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=max_tokens, temperature=0.4))
    return json.loads(response)["choices"][0]["text"]


"""

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)
print(json.loads(text_json)["choices"][0]["text"])
text_json = json.dumps(response)
"""


