
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



def twosum(arr,target):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i],arr[j])
                break


# def twosum_set(arr,target):
#     setnum = set()
#     for num in arr:
#         for num2 in arr:
#             if target - num - num2 not in setnum:
#                 setnum.add(num)
#                 # print(setnum)
#                 # print(num)
#             else:
#                 print(num,target-num)
#     print(setnum)
#
nums = [2,7,8,7,11, 15,23,55]
# # twosum(nums,38)
# twosum_set(nums,38)

def three_sum(newarr,target):
    newarr.sort()
    print(newarr)
    for i in range(len(newarr)-2):
        left = i +1
        right = len(newarr) -1

        while left<right:
            if newarr[left] == newarr[left -1]:
                continue
            tmp = newarr[i] + newarr[left] + newarr[right]
            if tmp == target:
                print(newarr[i],newarr[left],newarr[right])
                left= left +1
            elif tmp<target:
                left= left +1
            elif tmp>target:
                right=right-1

three_sum(nums,32)

# def twosum(target):
#     nums = [2, 7, 11, 15]
#     has_table ={}
#     for i in range(len(nums)):
#         if target - nums[i] not in has_table:
#             has_table[nums[i]] = i
#         else:
#             return has_table[target - nums[i]], i
#
#
# index_1, index_2 = twosum(17)
# print(index_1,index_2)