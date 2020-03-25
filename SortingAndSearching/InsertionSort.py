'''
idea was from COMP1405
Professor: Andrew Runka
'''

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
    insertion sort
    Function: insertionSort()
    Purpose: to sort an list in ascending order
    In: unsorted list
    Out: sorted list
'''


# def insertionSort(arr):
#     # start with an empty output list
#     out = []
#
#     # copy the input (to prevent mutation)
#     arr = arr[:]
#
#     # until the input is empty
#     while len(arr) > 0:
#
#         # take the first item out of input
#         item = arr.pop(0)
#
#         # add it to the end of output
#         out.append(item)
#
#         currentIndex = len(out) - 1
#         # while that item is out of order
#         while currentIndex > 0 and compare(out[currentIndex - 1], out[currentIndex]) == 1:
#             # swap left
#             temp = out[currentIndex]
#             out[currentIndex] = out[currentIndex - 1]
#             out[currentIndex - 1] = temp
#
#             currentIndex -= 1
#
#     # return the output list
#     return out

def insertionSort(unsortedList):
    lis = unsortedList[:]

    output = []

    while len(lis) != 0:
        item = lis.pop(0)

        output.append(item)

        index = len(output) - 1
        # swap left until its in place
        while index > 0 and output[index - 1] > output[index]:
            # swap
            temp = output[index - 1]
            output[index - 1] = output[index]
            output[index] = temp
            index = index - 1

        # output[index-1],output[index]=output[index],output[index-1]

    return output


def main():
    print("Test Insertion sort: ")
    numList = []
    for i in range(50):
        numList.append(random.randint(1, 500))
    print("Original list: ")
    print(numList)
    sortedList = insertionSort(numList)
    print("Sorted list: ")
    print(sortedList)

    print()

    print("Test bubble sort with string list: ")
    strList = ["zoo", "fun", "apple", "orange", "Newspaper", "Breakfast", "Lunch", "Dinner", "Vehicle"]
    print("Original list: ")
    print(strList)
    sortedStringList = insertionSort(strList)
    print("Sorted list: ")
    print(sortedStringList)


if __name__ == '__main__':
    main()
