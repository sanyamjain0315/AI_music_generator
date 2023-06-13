import requests

def freestyle(lyr,bpm, unique_identifier):

    lyr_lst = lyr.split(".")
    url = "https://api.uberduck.ai/tts/freestyle"
    payload = {
        "lyrics": [lyr_lst],
        "bpm": bpm,
        "voice": "zwf",
        "format": "json",
        "backing_track": "84a34767-12c0-4dc0-aa64-c292ac7d13c9"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic MTAzMjIxMDE0OToxMDMyMjEwMTQ5"
    }

    response = requests.post(url, json=payload, headers=headers)
    data=response.json()
    print(data)
    return data["mix_url"]
    
