import requests

client = requests.get("http://127.0.0.1:8000/cr/mixins/get-method/", headers="")
response = client.text

print(response)
