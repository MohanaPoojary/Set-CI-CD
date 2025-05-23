import json
import requests

head = {
    "Content-Type": "application/json"  
}
base_url = "https://reqres.in/api/users"

with open('./payload.json') as json_file:
    json_payload = json.load(json_file)

response = requests.post(url=base_url, headers=head, json=json_payload)

print("Status Code:", response.status_code)
print("Response:", response.text)
