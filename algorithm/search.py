# coding=utf-8
from sort import *

def linearSearch(arr, data):
    for i in range (len(arr)):
        if data == arr[i]:
            return True
    return False

def binarySearch(arr, data):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if data == arr[mid]:
            return True
        elif data < arr[mid]:
            high = mid - 1
        else:
            low = low + 1
    return False

if __name__ == "__main__":
    arr = [5,4,3,2,1,6,7,8,9,10,11]
    arr = bubbleSort(arr)

    print ("Input data :" ),
    data = int(raw_input())

    result = linearSearch(arr, data)
    result = binarySearch(arr, data)
    if result:
        print ("Found")
    else:
        print("Not found")
