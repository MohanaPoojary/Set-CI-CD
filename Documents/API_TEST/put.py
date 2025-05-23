import requests

headGet ={
    'accept': 'text/plain'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/1", headers=headGet)


print(response.json())
assert response.status_code == 200

# -----------------------------------------------


headPut = {
    'accept': 'text/plain',
    'Content-Type': 'application/json'
}

payload = {
  "id": 10,
  "title": "Mohan",
  "dueDate": "2025-05-21T18:19:12.848Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/1", headers=headPut, json=payload)

print(response.json())
assert response.status_code == 200


data = response.json()

assert data['id'] == 10
assert response.status_code == 200
