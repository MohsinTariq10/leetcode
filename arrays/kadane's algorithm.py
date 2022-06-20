class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cum_sum = 0
        max_sum = nums[0]
        for i in range(n):
            cum_sum += nums[i]
            if cum_sum > max_sum:
                max_sum = cum_sum
            if cum_sum <=0:
                cum_sum = 0
        return max_sum
            