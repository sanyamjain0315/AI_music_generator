from auth_keys import uberduck_auth
import json, requests
from time import sleep
from IPython.display import Audio
from prompt_to_lyrics import promt_to_lyrics

def paragraph_to_single_line(text):
    single_line = text.replace('\n', '').replace('\r', '')
    return single_line


def vocal_production(lyrics, uuid, bpm, unique_identifier):
    audio_uuid = requests.post(
        "https://api.uberduck.ai/speak",
        json=dict(speech=lyrics[:250], voicemodel_uuid=uuid, bpm=bpm),
        auth=uberduck_auth,
    ).json()["uuid"]

    # print("voics generated succesfully")
    # print(audio_uuid)
    # print("Sleeping for 5s \n")
    sleep(5)
    for t in range(10):
        sleep(2) # check status every second for 10 seconds.
        output = requests.get(
            "https://api.uberduck.ai/speak-status",
            params=dict(uuid=audio_uuid),
            auth=uberduck_auth,
        ).json()
        # print(output)
        if "path" in output:
            if output["path"] != None:
                audio_url = output["path"]
                print(audio_url)
                break


    # print("sleeping for 5s\n")

    sleep(5)
    return audio_url


    # print("making Audio file\n")
    with open(file_path, "wb") as file:
        file.write(response.content)

if __name__ =="__main__":
    lyr = "Uhh, that felt good Does it baby? Yeah, rub my back for me Where do you want me to rub it baby? Right here OK Ohh Turn around Aight, check it out though Why don't you put me on some music? What you wanna hear baby? Put me on some of that old gangsta shit Aight [ding dong] [needle scratching] Damn! the fuck is that, everytime i'm chillin someone ringing my motherfuckin doorbell You want me to get that for you? Yeah, handle that shit for me Aight, i'll be right back What the fuck?"
    uuid = "2c0c275e-f1ed-44a6-9797-bf67587365fa"
    vocal_production(lyrics=lyr,uuid=uuid,bpm=120)