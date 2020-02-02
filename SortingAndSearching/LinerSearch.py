import random

'''
    arr: List of number
    target: number, our target to find
'''
def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def test():
    numList = []
    for i in range(10):
        numList.append(random.randint(1,30))

    flag = linearSearch(numList, 20)
    print(numList)
    if flag == True:
        print("FOUND!!!")
    else:
        print("NOT FOUND!!!")

test()