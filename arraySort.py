def arraySort(unsorted_array):
  uniqueArray = list(set(unsorted_array))
  occur = {}
  mean = 0
  pos = []
  neg = []
  SortedArr = []
  for el in unsorted_array:
    if el in occur:
      occur[el] += 1
    else:
      occur[el] = 1
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

  for number in (neg_arr):
    if number != None:
      SortedArr += [number + mean - largestNegativeEl] * occur[number + mean - largestNegativeEl]
  for number in pos_arr:
    if number != None:
      SortedArr += [number + mean + smallestPositiveEl] * occur[number + mean + smallestPositiveEl]
  return (SortedArr)


