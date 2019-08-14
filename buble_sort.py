def buble_sort(arr):
	for i in range(len(arr) - 1):
		for j in range(len(arr) -1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
	return arr

if __name__ == "__main__":
	arr = [8,9,0,2,3,6,1,2,]
	arr = buble_sort(arr)
	print(arr)