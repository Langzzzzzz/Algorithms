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


'''
    Advanced bubbleSort
    Function: advancedBubbleSort()
    Purpose: to sort an list in ascending order
    In: unsorted list
    Out: sorted list
'''

def advancedBubbleSort(arr):
    size = len(arr)
    for i in range(size):
        # flag to check that adjacent elements swapped or not
        check = 0
        for j in range(size - 1 - i):
            # compare adjacent element
            if compare(arr[j], arr[j + 1]) == 1:
                # swap adjacent element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                check += 1
        # if adjacent elements not swapped which means the list already sorted
        if check == 0:
            break
    return


def test():
    print("Test Basic bubble sort: ")
    numList = []
    for i in range(50):
        numList.append(random.randint(1, 500))
    print("Original list: ")
    print(numList)
    bubbleSort(numList)
    print("Sorted list: ")
    print(numList)

    print()

    print("Test Advanced bubble sort: ")
    advList = []
    for i in range(50):
        advList.append(random.randint(1, 500))
    print("Original list: ")
    print(advList)
    advancedBubbleSort(advList)
    print("Sorted list: ")
    print(advList)

    print()

    print("Test bubble sort with string list: ")
    strList = ["zoo", "fun", "apple", "orange", "Newspaper", "Breakfast", "Lunch", "Dinner", "Vehicle"]
    print("Original list: ")
    print(strList)
    bubbleSort(strList)
    print("Sorted list: ")
    print(strList)


test()
