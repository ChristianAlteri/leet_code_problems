class Solution(object):
    def maxSubArray(self, nums):

        maxSub = nums[0]
        curSum = 0
        # a = 21
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            # print('CURRENT ' ,curSum)
            maxSub = max(maxSub, curSum)
            # print('MAX ' ,maxSub)
        return maxSub
        # have a total_sum and total_sum_array to store sum and to track numbers
        # prev_total_sum = total_sum + i[n]
        # if total_sum < prev_total_sum then you have found the max number