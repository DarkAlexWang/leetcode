def numberOfItemsInRange(s, r):
    numItemsInCompartment = 0
    loadingItems = 0
    insideCompartment = False
    for i in range(r[0]-1, r[1]):
        if s[i] == '|':
            if insideCompartment:
                numItemsInCompartment += loadingItems
                loadingItems = 0
            else:
                insideCompartment = True
        elif insideCompartment:
            loadingItems += 1
    return numItemsInCompartment

def numberOfItems(s, startIndices, endIndices):
    ranges = []
    for i, j in zip(startIndices, endIndices):
        ranges.append((i, j))

    num_items = []
    for range in ranges:
        num_items.append(numberOfItemsInRange(s, range))
    return num_items

if __name__ == '__main__':
    print(numberOfItems('|**|*|*', [1, 1], [5, 6]))
