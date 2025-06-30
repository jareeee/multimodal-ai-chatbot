import requests
client_id = "536eff53c3e4083"

def upload_image_to_imgur(image_path: str):
    headers = {
        "Authorization": f"Client-ID {client_id}"
    }
    with open(image_path, "rb") as img_file:
        payload = {
            "image": img_file.read()
        }
        response = requests.post("https://api.imgur.com/3/image", headers=headers, files=payload)

    if response.status_code != 200:
        raise Exception(f"Upload failed: {response.status_code} - {response.text}")

    return response.json()["data"]["link"]
