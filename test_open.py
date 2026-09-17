import requests

response = requests.post(
    "http://localhost:8081/apps/open",
    json={"name": "notepad"}
)

print(response.status_code)
print(response.text)