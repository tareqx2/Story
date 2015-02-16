import requests
from flask import Flask, jsonify
from flask import abort
from flask import request
from bs4 import BeautifulSoup


IMDB_RANDOM = "http://www.imdb.com/random/title"

resp = requests.get(IMDB_RANDOM)
response = {}
soup = BeautifulSoup(resp.text)
description = soup.findAll("p", { "itemprop" : "description" })
response["description"] = description
movieName = soup.findAll("span",{"itemprop": "name"})
response["name"] = movieName[0].get_text()
soup2 = soup.findAll("div", { "itemprop" : "description"})
storyline = BeautifulSoup(soup2[0].get_text())
storyline = storyline.findAll("p")
response["storyline"] = storyline

print response
