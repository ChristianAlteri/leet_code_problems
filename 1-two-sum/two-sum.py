class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                # print("success")
                # print([map[diff], i])
                return [map[diff], i]
            map[num] = i    
            # print(map)

