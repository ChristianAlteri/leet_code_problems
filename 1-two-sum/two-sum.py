class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                # print(sum)
                if sum == target:
                    # print(i, j)
                    return i, j
                    # print("hello")

