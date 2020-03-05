def arraySortStrings(line):
    occurances = {}
    l = list(line)
    for x in range(len(l)):
        l[x] = ord(l[x])

        if l[x] in occurances:
            occurances[l[x]] += 1
        else:
            occurances[l[x]] = 1

    sortedUnique = [None] * (max(l) + 1)

    for x in range(len(l)):
        sortedUnique[l[x] - min(l)] = l[x]-min(l)
    sortedUnique = list(filter(None.__ne__, sortedUnique))
    
    SortedArr = []
    for f in sortedUnique:
        SortedArr += [ chr( f + min(l) ) ] * occurances[f + min(l)]
    
    return SortedArr
    