


class game(object):
  def __init__(self, logid):
    self.logid=logid
  def __repr__(self):
    return (str("GAMEOBJECT,ID:"+self.logid))
  def initdata(self,data):
    self.info=data["info"]
    self.teams=data["teams"]
    self.length=data["length"]
    self.players=data["players"]
    self.chat=data["chat"]
  def statstotal(self, steamid):
    return self.players[steamid]
  def get(self,steamid,thing):
    return self.players[steamid][thing]
  def playerlist(self):
    result=[]
    for key in self.players.keys():
      result.append(key)
    return result
  def stats(self,player):
    return(self.players[player.steamid3])
print("game guapo")