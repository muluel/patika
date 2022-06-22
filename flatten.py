def flatten(x,y=list()):
  for i in x:
    if type(i) != list:
      y.append(i)
    else:
      flatten(i)
  return y

q=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flatten(q)