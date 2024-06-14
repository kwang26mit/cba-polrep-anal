# huggingface
import os
import transformers
import torch

# ollama
import requests
import json

# os.environ['HF_TOKEN'] = "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" # huggingface
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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" # huggingface
url = "https://localhost:11434/api/chat" # ollama

# def llama3_hf(prompt):
#     model_id = "meta-llama/Meta-Llama-3-8B"

#     pipeline = transformers.pipeline(
#         "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
#     )
#     response = pipeline(prompt)
#     return response

def llama3_ollama(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    headers = {
        "Content-Type": 'application/json'
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['message']['content']

# print(llama3_hf("Who wrote Harry Potter?"))
print(llama3_ollama("Who wrote Harry Potter?"))
