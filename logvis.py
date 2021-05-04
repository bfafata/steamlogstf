import requests
import json
import operator
import html
import time
import sys
inp="[U:1:112892780]"



class loglist(object):
  def __init__(self,steamid,limit=10):
    self.steamid=steamid
    self.limit=limit
    self.list_data={"player":str(self.steamid), "limit":str(self.limit)}
    self.list_response = requests.get("https://logs.tf/api/v1/log",params=self.list_data)
    self.list_json=json.loads(self.list_response.text)
  def __repr__(self):
    return (f"{self.steamid}LIST, length {self.limit}")


class player(object):
  def __init__(self, steamid3): #steam id 3
    self.steamid3=steamid3

    self.sr_player_data={"q":srurl(steamid3)}
    #self.sr_player_response=requests.get(f"https://steamrep.com/search?q={srurl(steamid3)}")
    #self.sr_player_str=str(self.sr_player_response.text)
    #self.sr_player_response_data=strfind(self.sr_player_str, "<div id=\"steamids\">","</div>")

    #self.alias= strfind(self.sr_player_response_data, "steamname: ","\n")
    #self.steamid= strfind(self.sr_player_response_data, "https://steamcommunity.com/profiles/","\n")
  def __repr__(self):
    return self.steamid
  def __eq__(self,other):
    return self.steamid==other.steamid

def srurl(id3):
  return "%5BU%3A1%3A"+id3[5:len(id3)-1]+"%5D"

def strfind(string,beginning,end):
  init=string.find(beginning)
  fin=string[init:].find(end)
  return string[init+len(beginning):init+fin]

class game(object):
  def __init__(self, data, idx, title, gamemap):
    self.data=data
    self.idx=idx
    self.title=title
    self.gamemap=gamemap
    self.version=data["version"]
    self.teams=data["teams"]
    self.length=data["length"]
    self.players=data["players"]
    self.chat=data["chat"]
  def __repr__(self):
    return (str(self.idx)+self.title+self.gamemap)
  def print():
    returnp(self.data)
  def statstotal(self, steamid):
    return self.data["players"][steamid]
  def get(self,steamid,thing):
    return self.data["players"][steamid][thing]
  def playerlist(self):
    result=[]
    for key in self.players.keys():
      result.append(key)
    return result
  def stats(self,player):
    return(self.players[player.steamid3])

def p(x):
  print(json.dumps(x,indent=2))

gamelist=[]
def getgames(loglist):
  start=time.time()
  for item in loglist.list_json["logs"]:
    start=time.time()
    idx=item["id"]
    title=item["title"]
    gamemap=item["map"]
    response=requests.get("https://logs.tf/json/"+str(idx))
    print(response.status_code,response.url)
    gamedata=json.loads(response.text)
    globals()[f"game{idx}"]=game(gamedata,idx,title,gamemap)
    gamelist.append(idx)
    print("SUCCESS: loaded")
  end=time.time()
  print("elapsed",start-end)


def getstats():
  totaltime=0
  totalkills=0
  totalassists=0
  totaldeaths=0
  totaldamage=0
  for item in gamelist:
    print("getting stats for game",item)
    selectedgame=globals()[f"game{item}"]
    totaltime+=selectedgame.length
    totalkills+=selectedgame.get(inp,"kills")
    totalassists+=selectedgame.get(inp,"assists")
    totaldeaths+=selectedgame.get(inp,"deaths")
    totaldamage+=selectedgame.get(inp,"dmg")
  return (totaltime,totalkills,totalassists,totaldeaths,totaldamage)

#me=player(inp)
#mylist=loglist(me.steamid)

#getgames(mylist)
