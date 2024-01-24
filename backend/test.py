import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-13b-chat-hf"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)