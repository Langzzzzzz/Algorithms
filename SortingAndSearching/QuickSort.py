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

print(quickSort([10,23,1,8,123,9,2130,1230]))