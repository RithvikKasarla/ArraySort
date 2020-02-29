def remove_copys(ar):
  copy = ar
  doubs = {}
  for idx, x in enumerate(ar):
    if x in doubs:
      doubs[x] += 1
    else:
      doubs[x] = 1

  return list(set(copy)),doubs

def arraySort(x_b):
  x,occur = remove_copys(x_b)
  s = 0
  pos = []
  neg = []
   
  for el in x:
    s += el
  s= int(s/len(x))

  for el in range(0,len(x)):
    x[el] = x[el]-s
    if x[el] >=0:
      pos.append(x[el])
    else:
      neg.append(x[el])

  #mp = max(pos)
  pm = min(pos)

  mn = max(neg)
  #nm = min(neg)
  
  pos_f = [None] * int(max(pos) - pm + 1)
  neg_f = [None] * (int(min(neg) + mn - 1) * -1)

  for z in range(len(pos)):
    pos_f[pos[z] - pm] = pos[z] - pm

  for y in range(len(neg)):
    neg_f[neg[y] + mn] = neg[y] + mn

  neg_f = list(filter(None.__ne__, neg_f))
  pos_f = list(filter(None.__ne__, pos_f))

  final = []
  for x in pos_f:
    final.append(x + s + pm)
  
  for y in reversed(neg_f):
    final.insert(0, y + s - mn)

  trueFinal = []
  for f in final:
    trueFinal += [f] * occur[f]
  return (trueFinal)


