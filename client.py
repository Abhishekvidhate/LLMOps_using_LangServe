import requests

response = requests.post(
    "https://localhost:8000/eassay/invoke",
    json={'input': {'topic': "my best friend"}}
)

print(response.json()['output']['content'])
