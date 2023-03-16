import requests
# from getpass import getpass

# getpass()
auth = requests.post(
    "http://127.0.0.1:8000/cr/auth/", 
    json={"username": "legion", "password": "20051205"}
)

print(auth.json())
if auth.status_code == 200:
    auth_token = auth.json()["token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    fetch_data = requests.get("http://127.0.0.1:8000/cr/mixins/get-method/", headers=headers)
    response = fetch_data.json()
    print(response)
