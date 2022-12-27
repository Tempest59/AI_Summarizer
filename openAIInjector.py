import openai
import json

OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY




def summarizeAi(text, max_tokens):
    prompt = "Summarize this text by rewriting it in an academical and detailed style. Text: '" + text + "' Prompt:"
    response = json.dumps(openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=max_tokens, temperature=0.9))
    return json.loads(response)["choices"][0]["text"]


"""

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=10)
print(json.loads(text_json)["choices"][0]["text"])
text_json = json.dumps(response)
"""


