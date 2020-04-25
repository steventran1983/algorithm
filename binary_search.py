def binary_search(arr,start,end,target):
    if end >= start:
        mid = start + (end - start)//2
        if arr[mid] == target:
            print(mid)
        elif arr[mid] >= target:
            binary_search(arr,start,mid -1,target)
        else:
            binary_search(arr,mid+1,end,target)
    else:
        return "Khongco"

arr = [1,3,5,7,8,67,77,88,99,120]
# binary_search(arr,0,len(arr)-1,3)



def binarySearch(arr,start,end,target):

    if end>start:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return(mid)
        elif arr[mid] > target:
            return binarySearch(arr,start,mid - 1,target)
        elif arr[mid] < target:
            return binarySearch(arr, mid+1, end, target)
    else:
        return -1

print(binarySearch(arr,0,len(arr)-1,200))
