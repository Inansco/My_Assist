import requests

response = requests.get("http://localhost:8081/health")

print(response.text)