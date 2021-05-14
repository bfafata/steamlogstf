import requests
import json
import operator
import html
import time
import sys
import pathlib

import classes

inp="[U:1:112892780]"
myid="76561198073158508"
def p(x):
  print(json.dumps(x,indent=2))

gamelist=[]

def definePlayerObject(id):
  localobject=classes.player(id)
  globals()["P"+id]=localobject

def defineLoglistFromPlayerObject(player):
  localobject=classes.loglist(player.steamid)
  globals()["LL"+player.steamid]=localobject

def defineGameFromID(gameid):
  localobject=classes.game(gameid)
  globals()["game"+gameid]=localobject

def fillGameData(gameid):
  response=requests.get("https://logs.tf/json/"+str(gameid))
  print(response.status_code,response.url)
  gamedata=json.loads(response.text)
  globals()["game"+gameid].initdata(gamedata)

gamelist=[]
def getGames(id):
  start=time.time()
  definePlayerObject(id)
  defineLoglistFromPlayerObject(globals()["P"+id])
  localloglist=globals()[f"LL{id}"].list_json["logs"]
  for item in localloglist:
    defineGameFromID(str(item["id"]))
    fillGameData(globals()["game"+str(item["id"])].logid)
    gamelist.append("game"+str(item["id"]))
  end=time.time()
  print("elapsed",start-end)


resultDict=dict()
measureStats=["kills","assists","deaths","dmg_real"]
def initResultDict():
  for stat in measureStats:
    resultDict[stat]=0

def getPlayerStats(player):
  player.fetchfromSI3()
  for item in gamelist:
    for stat in measureStats:
      print("getting stats for game",item)
      selectedgame=globals()[item]
      resultDict[str(stat)]+=selectedgame.get(player.steamid3,stat)

getGames(myid)
#class is P76561198073158508
initResultDict()
getPlayerStats(P76561198073158508)

json.dump(resultDict,open("myfile.txt","w"))