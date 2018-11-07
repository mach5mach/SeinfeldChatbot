import scrapy
from scrapy.crawler import CrawlerProcess

import subprocess
import json

command =  "scrapy runspider seinfeldepisodes.py -t json --nolog -o - > seinfeldepisodes.json"
#gets list of episodes and places them into seinfeldepisodes.json
subprocess.call(command, shell=True)

#for each episode in seinfeldepisodes.json, run spider on page
with open("seinfeldepisodes.json") as f:
    episodes = json.load(f)

for episode in episodes:
    url = 'http://www.seinfeldscripts.com/' + episode["link"]
    output = "episodes_raw/" + episode["number"] + ".json"
    command =  "scrapy runspider seinfeldepisode.py -t json --nolog -a start_urls=\"%s\" -o - > %s" % (url, output)
    subprocess.call(command, shell=True)
