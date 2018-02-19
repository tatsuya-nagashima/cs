def bubbleSort(arr):
    for i in range (len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp      = arr[j]
                arr[j]   = arr[j+1]
                arr[j+1] = tmp

    return arr

def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range (i+1, len(arr)-1):
            if arr[min] > arr[j]:
                min = j
            tmp      = arr[i]
            arr[i]   = arr[min]
            arr[min] = tmp

    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j-1]:
                break
            else:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp

    return arr


if __name__ == "__main__":
    arr = [5,4,3,2,1,6,7,8,9,10]

    print("before", arr)
    #bubbleSort(arr)
    #selectionSort(arr)
    insertionSort(arr)
    #quickSort(arr)
    print("after ", arr)
