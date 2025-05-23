import requests

head = {
    'Authorization': 'Bearer 114418a2f4f523a9f4be54b24c25c1b743ee32547829ae3859787480dca301d3',
    'Content-Type': 'application/json'
}

body = {"id":7899584,"name":"Sitara Kaur","email":"sitssarssa_kaur@roassssdriguez-krajcik.example","gender":"male","status":"active"}  

url = "https://gorest.co.in/public/v2/users"
response = requests.post(url, headers= head, json= body)

if response.status_code == 201:
    user_id = response.json()['id']
    responseGet = requests.get(f"{url}/{user_id}", headers=head)
    print("get response:", responseGet.json())

else:
    print(response.status_code)
    print("User Not Created:", response.json())

