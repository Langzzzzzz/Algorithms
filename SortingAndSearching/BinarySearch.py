import random

from SortingAndSearching.InsertionSort import insertionSort

'''
    Notice: Only work for sorted list
    purpose: To check target is in the list or not
    arr: List of number
    target: number, our target to find
'''

def binarySearch(arr, target):
    low = 0
    high = len(arr)
    # base case to stop
    while low <= high:
        median = (low + high) // 2
        # found target in the list
        if arr[median] == target:
            return True
        else:
            # if median greater than target, only find in first half
            if arr[median] > target:
                high = median - 1
            # if median smaller than target, only find in second half
            else:
                low = median + 1
    return False


def main():
    numList = []
    for i in range(10):
        numList.append(random.randint(1, 30))
    sortedNumList = insertionSort(numList)
    flag = binarySearch(sortedNumList, 20)
    print(sortedNumList)
    if flag:
        print("FOUND!!!")
    else:
        print("NOT FOUND!!!")

if __name__ == '__main__':
    main()
