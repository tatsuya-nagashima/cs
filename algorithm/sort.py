def bubbleSort(arr):
    for i in range (len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp      = arr[j]
                arr[j]   = arr[j+1]
                arr[j+1] = tmp
    return arr

if __name__ == '__main__':
    arr = [5,4,3,2,1]
    print bubbleSort(arr)
