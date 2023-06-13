from bardapi import Bard
from auth_keys import bard_api_key
import re, json


def remove_pattern_from_text(text):
    pattern = r"\((.*?)\)"
    text = re.sub(pattern, "", text)

    if "**" in text:
        pattern = r"\*\*(.*?)\*\*"
        text = re.sub(pattern, "", text)
    return text

def clean(str):
    if "```" in str:
        index = str.index("```")
        return remove_pattern_from_text(str[index+3:-3])
    elif ":" in str:
        index = str.index(":")
        return remove_pattern_from_text(str[index+1:])


def parse_json(json_string):
    cleaned_string = re.sub(r"[\x00-\x1F\x7F]", "", json_string)
    
    # Parse the cleaned JSON data
    json_data = json.loads(cleaned_string)
    return json_data
    

def promt_to_lyrics(prompt):
    bard = Bard(token=bard_api_key)
    raw_answer = bard.get_answer("Write lyrics for a song about about'"+prompt+"'  of the lyrics, suitable tilte,bpm, and no of bars for the song, club all the things in  json, the json file should have title, lyrics,bpm, bars. Only return json file and no extra text")['content']
    raw_answer+="."
    print(raw_answer)
    json_str = raw_answer[raw_answer.index("{"):raw_answer.index("}")+1]
    # print(json_str)
    return parse_json(json_str)


if __name__ =="__main__":
    prompt = input("Topic/decsription of the song: ")
    jfile = promt_to_lyrics(prompt)

    print(jfile["title"])
    print(jfile["bars"])
    print(jfile["lyrics"][0])
    print(jfile["bpm"])
