import requests

def upload_to_salesforce(file_path):
    url = "https://salesforce/api/upload"
    headers = {"Authorization": "Bearer <TOKEN>"}

    with open(file_path, "rb") as f:
        files = {"file": f}
        requests.post(url, headers=headers, files=files)
