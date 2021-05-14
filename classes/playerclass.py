import requests
def srurl(id3):
  return "%5BU%3A1%3A"+id3[5:len(id3)-1]+"%5D"

def strfind(string,beginning,end):
  init=string.find(beginning)
  fin=string[init:].find(end)
  return string[init+len(beginning):init+fin]

class player(object):
  def __init__(self, steamid="", data=[]):
    self.steamid=steamid
    self.data=data

    #self.alias= strfind(self.sr_player_response_data, "steamname: ","\n")
    #self.steamid= strfind(self.sr_player_response_data, "https://steamcommunity.com/profiles/","\n")
  
  def fetchfromSI3(self):
    self.sr_player_response=requests.get(f"https://steamrep.com/search?q={self.steamid}")
    self.sr_player_str=str(self.sr_player_response.text)
    self.sr_player_response_data=strfind(self.sr_player_str, "<div id=\"steamids\">","</div>")
    self.steamid3=strfind(me.sr_player_response_data,"3ID: ", "\n")
    print("success")
  def __repr__(self):
    return self.steamid
  def __eq__(self,other):
    return self.steamid==other.steamid
myid="76561198073158508"
me=player(myid)
me.fetchfromSI3()
print("player guapo")
