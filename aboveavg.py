def aboveaverage(l):
  aggregate = {}
  innings = {}
  totalscore = 0
  totalinnings = 0
  for (name,score) in l:
    totalscore += score
    totalinnings += 1
    try:
      aggregate[name] += score
      innings[name] += 1
    except KeyError:
      aggregate[name] = score
      innings[name] = 1

  overallaverage = totalscore/totalinnings

  aboveaverage = []
    
  for name in aggregate.keys():
    average = aggregate[name]/innings[name]
    if average >= overallaverage: 
      aboveaverage.append(name)
      
  return(sorted(aboveaverage))
