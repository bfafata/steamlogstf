import requests
import json

class loglist(object):
  def __init__(self,steamid,limit=10):
    self.steamid=steamid
    self.limit=limit
    self.list_data={"player":str(self.steamid), "limit":str(self.limit)}
    self.list_response = requests.get("https://logs.tf/api/v1/log",params=self.list_data)
    self.list_json=json.loads(self.list_response.text)
  def __repr__(self):
    return (f"{self.steamid}LIST, length {self.limit}")
  def len(self):
    return len(self.list_json["logs"])

