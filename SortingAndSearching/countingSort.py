def countingSort(lis, k):
    output = []

    c = []
    for i in range(k):
        c.append(0)

    # count all the items
    for ele in lis:
        c[ele] += 1  # note: using the item as the index!!

    for i in range(len(c)):  # for each counter
        for j in range(0, c[i]):  # add that many copies
            output.append(i)

    return output