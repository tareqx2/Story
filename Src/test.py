import requests
from flask import Flask, jsonify
from flask import abort
from flask import request
from bs4 import BeautifulSoup
import json

IMDB_RANDOM = "http://www.imdb.com/random/title"
resp = requests.get(IMDB_RANDOM)
response = {}
soup = BeautifulSoup(resp.text)
description = soup.findAll("p", { "itemprop" : "description" })
response["description"] = description[0].get_text()
movieName = soup.findAll("span",{"itemprop": "name"})
response["Name"] = movieName[0].get_text()
soup2 = soup.findAll("div", { "itemprop" : "description" })

if (not soup2):
	storyline = BeautifulSoup(soup2[0].get_text())
	storyline = storyline.findAll("p")
	response["storyline"] = storyline[0].get_text()

print json.dumps(response)
