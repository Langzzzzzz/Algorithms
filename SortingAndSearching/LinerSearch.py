import random

'''
    purpose: To check target is in the list or not
    arr: List of number
    target: number, our target to find
'''

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

def main():
    numList = []
    for i in range(10):
        numList.append(random.randint(1,30))

    flag = linearSearch(numList, 20)
    print(numList)
    if flag == True:
        print("FOUND!!!")
    else:
        print("NOT FOUND!!!")

if __name__ == '__main__':
    main()