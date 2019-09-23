def count_maximum(str):
	ACSII = 256 
	arr_count = [0] * ACSII
	for character in str:
		arr_count[ord(character)] = arr_count[ord(character)] + 1
	max_value = -1
	max_index = -1;
	for i in range(len(arr_count)):
		if arr_count[i] > max_value:
			max_value = arr_count[i]
			max_index = i
	print(max(arr_count))
	return max_index,max_value

if __name__ == "__main__":
	max_index,max_value = count_maximum("today is the first day in schoolddddddddddddddd")
	print("{}: {}".format(chr(max_index),max_value))