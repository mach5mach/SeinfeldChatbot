import json
from os import listdir
import os

def get_character(name):
    dir = "episodes_clean/"
    files = listdir(dir)

    chardir = "characters/"
    charfile = name + ".txt"
    character = []

    for file in files:
        with open(dir + file) as rf:
            episode = json.load(rf)

            for item in episode:
                if "line" not in item:
                    continue
                if len(item["line"]) > 0:
                    if(item["line"][0].lower().startswith(name.lower() + ": ")):
                        str = item["line"][0][len(name + ": "):]
                        character.append({"line": str})

        with open(chardir + charfile, "w") as cf:
            for item in character:
                cf.write(item["line"].encode("utf-8") + "  ", )

get_character("Jerry")
