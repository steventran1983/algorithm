
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twosum(target):
    nums = [2, 7, 11, 15]
    has_table ={}
    for i in range(len(nums)):
        if target - nums[i] not in has_table:
            has_table[nums[i]] = i
        else:
            return has_table[target - nums[i]], i


index_1, index_2 = twosum(17)
print(index_1,index_2)