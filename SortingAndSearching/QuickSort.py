# think about Divide and Conquer
def quickSort(arr):
    less = []
    greater = []
    # base case
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        for i in arr[1:]:
            if i > pivot:
                greater.append(i)
            else:
                less.append(i)
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([23,10]))