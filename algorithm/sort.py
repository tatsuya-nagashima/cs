# coding=utf-8

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

def _quickSort(arr, left, right):
    if left >= right:
        return arr

    pivot = median(arr[left], arr[(left+right)//2], arr[right])
    l = left
    r = right

    while True:
        while arr[l] < pivot:
            l += 1
        while pivot < arr[r]:
            r -= 1
        if (r <= l):
            break

        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
        l += 1
        r -= 1

    _quickSort(arr, left, l - 1)
    _quickSort(arr, r + 1, right)

    return arr

def quickSort(arr):
    return _quickSort(arr, 0, len(arr)-1)

def median(x, y, z):
    if x < y:
        if y < z:
            return y
        elif x < z:
            return z
        else:
            return x
    else:
        if x < z:
            return x
        elif y < z:
            return z
        else:
            return y


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])

    return merged

if __name__ == "__main__":
    arr = [5,4,3,2,1,6,7,8,9,10]

    print("before", arr)
    #bubbleSort(arr)
    #selectionSort(arr)
    #insertionSort(arr)
    quickSort(arr)
    #mergeSort(arr)
    print("after ", arr)
