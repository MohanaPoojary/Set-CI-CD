import requests

def test_get_request_validation():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "Janet"
    print("response:", response.json())
