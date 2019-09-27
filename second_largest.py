def second_lagest(arr):
    max_1 = -1
    max_2 = -2

    for num in arr:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2 and num < max_1:
            max_2 = num

    return max_2

print(second_lagest([3,5,1,6,7,8,2,89,8,10]))

print(second_lagest([100,5,1,6,7,8,2,89,8,10]))