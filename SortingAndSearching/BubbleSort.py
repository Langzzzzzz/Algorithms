import random

'''
    Function: compare()
    Purpose: compare int or string
    In: 2 elements
    Out: integer
'''
def compare(a, b):
    if a >= b:
        return 1
    else:
        return 0


'''
    Basic bubbleSort
    Function: bubbleSort()
    Purpose: to sort an list in ascending order
    In: unsorted list
    Out: sorted list
'''
def bubbleSort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size - 1 - i):
            # compare adjacent element
            if compare(arr[j], arr[j + 1]) == 1:
                # swap adjacent element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return


def test():
    numList = []
    for i in range(10):
        numList.append(random.randint(1, 30))
    print("Original list: ")
    print(numList)
    bubbleSort(numList)
    print("Sorted list: ")
    print(numList)

    strList = ["zoo", "fun", "apple", "orange", "Newspaper", "Breakfast", "Lunch", "Dinner", "Vehicle"]
    print("Original list: ")
    print(strList)
    bubbleSort(strList)
    print("Sorted list: ")
    print(strList)


test()
