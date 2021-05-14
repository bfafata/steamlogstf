import logimport

def getstats():
  totaltime=0
  totalkills=0
  totalassists=0
  totaldeaths=0
  totaldamage=0
  for item in logimport.gamelist:
    print("getting stats for game",item)
    selectedgame=globals()[f"game{item}"]
    totaltime+=selectedgame.length
    totalkills+=selectedgame.get(inp,"kills")
    totalassists+=selectedgame.get(inp,"assists")
    totaldeaths+=selectedgame.get(inp,"deaths")
    totaldamage+=selectedgame.get(inp,"dmg")
  return (totaltime,totalkills,totalassists,totaldeaths,totaldamage)
