def remove_copys(ar):
  occurances = {}
  for x in ar:
    if x in occurances:
      occurances[x] += 1
    else:
      occurances[x] = 1

  return list(set(ar)),occurances

def arraySort(unsorted_array):
  uniqueArray,occur = remove_copys(unsorted_array)
  mean = 0
  pos = []
  neg = []
   
  for el in uniqueArray:
    mean += el
  mean= int(mean / len(uniqueArray ) )

  for el in range(0,len(uniqueArray)):
    uniqueArray[el] = uniqueArray[el]-mean
    if uniqueArray[el] >=0:
      pos.append(uniqueArray[el])
    else:
      neg.append(uniqueArray[el])

  smallestPositiveEl = min(pos)

  largestNegativeEl = max(neg)
  
  pos_arr = [None] * int(max(pos) - smallestPositiveEl + 1)
  neg_arr = [None] * (int(min(neg) + largestNegativeEl - 1) * -1)

  for z in range(len(pos)):
    pos_arr[pos[z] - smallestPositiveEl] = pos[z] - smallestPositiveEl

  for y in range(len(neg)):
    neg_arr[neg[y] + largestNegativeEl] = neg[y] + largestNegativeEl

  for number in reversed(neg_arr):
    if number != None:
      SortedArr = [number + mean - largestNegativeEl] * occur[number + mean - largestNegativeEl]
  for number in pos_arr:
    if number != None:
      SortedArr = [number + mean + smallestPositiveEl] * occur[number + mean + smallestPositiveEl]
  return (SortedArr)


