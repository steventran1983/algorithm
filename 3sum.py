# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    array = []
    for i in range(0, len(nums) - 2):
        hash_table = {}

        for j in range(i + 1, len(nums) - 1):
            if -(nums[i] + nums[j]) in hash_table:
                temp = [nums[i], nums[j], -(nums[i] + nums[j])]
                temp.sort()
                if temp not in array:
                    array.append(temp)
            else:
                hash_table[nums[j]] = j
    return array


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))