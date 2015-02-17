import requests
from flask import Flask, jsonify
from flask import abort
from flask import request
from bs4 import BeautifulSoup
import json

IMDB_RANDOM = "http://www.imdb.com/title/tt0045793/?ref_=fn_al_tt_1"
resp = requests.get(IMDB_RANDOM)
response = {}
soup = BeautifulSoup(resp.text)
print resp.text
description = soup.findAll("p", { "itemprop" : "description" })
response["description"] = description[0].get_text()
movieName = soup.findAll("span",{"itemprop": "name"})
response["Name"] = movieName[0].get_text()

soup2 = soup.findAll("div", { "itemprop" : "description" })

response["storyline"] = soup2[0].get_text()

print json.dumps(response)
