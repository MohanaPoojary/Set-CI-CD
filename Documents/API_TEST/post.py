import requests

head = {
    'accept': 'text/plain',
    'Content-Type': 'application/json'
}

payload = {
  "id": 1,
  "title": "Mohan",
  "dueDate": "2025-05-21T18:19:12.848Z",
  "completed": True
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities/", headers=head, json=payload)

print(response.status_code)
print(response.json())

data = response.json()

assert data['id'] == 1
assert response.status_code == 200
