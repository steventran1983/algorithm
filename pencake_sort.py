def max_value(arr,end):
    max_value = -999
    max_position = 0
    for i in range(end):
        if arr[i] >= max_value:
            max_value = arr[i]
            max_position = i
    return max_position

def flip(arr,k):
    i = 0
    while i < k:
        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp
        i= i+ 1
        k = k-1
    return arr

def pencake_sort(arr):
    i = len(arr)
    length = len(arr)
    while i >0:
        max_pos = max_value(arr, length)
        print(arr)
        print(max_pos)
        flip(arr, max_pos)
        print(arr)
        flip(arr, length -1)
        print(arr)
        print(length)
        length = length -1
        i = i -1
        print("*************************************")
    return arr

arr = [1,5,6,7,10,9]

print(pencake_sort(arr))