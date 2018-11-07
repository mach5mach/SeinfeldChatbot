import json
from os import listdir
import os

rawdir = "episodes_raw/"
rawfiles = listdir(rawdir)
cleandir = "episodes_clean/"
cleandata = {}

for rawfile in rawfiles:
    with open(rawdir + rawfile) as rf:
        episode = json.load(rf)

        for item in episode:

            if "line" not in item:
                continue
            elif len(item["line"]) > 0:
                if type(item["line"][0]) is unicode:
                    item["line"][0] = item["line"][0].encode("utf-8")

                item["line"][0] = item["line"][0].replace("\n", " ")

        cleanname = cleandir + os.path.basename(rf.name)
        with open(cleanname, "w") as cf:
            json.dump(episode, cf)
