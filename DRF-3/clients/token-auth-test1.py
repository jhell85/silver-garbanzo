import requests

def client():
    # data = { "username": "restTest" , "email": "test@rest.com", "password1": "changeme123", "password2": "changeme123"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                         data=data)

    token_h = "Token bdc0255400ea4de7da4df715b284c4a01a2c69d9"

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()