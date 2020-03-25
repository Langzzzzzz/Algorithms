def selectionSort(lis):
    lis = lis[:]  # breaks the alias (creates a local copy)
    # lis += []
    # lis = copyList(lis)

    # create an empty output list
    output = []
    # until the input list is empty:
    while len(lis) != 0:
        i = findSmallest(lis)
        small = lis.pop(i)
        output.append(small)
    return output


def findSmallest(lis):
    #find smallest element in the list and return the index
    smallestIndex = 0
    for i in range(1, len(lis)):
        if lis[i] < lis[smallestIndex]:
            smallestIndex = i

    return smallestIndex