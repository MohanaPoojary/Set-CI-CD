import requests

para = {
    "page": 1,
    "per_page": 3
}
url = "https://gorest.co.in/public/v2/users"
respose = requests.get(url, params=para)

# print(respose.json())
if respose.status_code == 200:
    print("Response:", respose.json())
else:
    print(respose.status_code)