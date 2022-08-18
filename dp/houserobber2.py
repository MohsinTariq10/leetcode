class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
    
    def rob1(self, nums):
        n = len(nums)
        a = 0
        b = nums[0]
        for i in range(1, n):
            left = nums[i]
            if i-2>-1: left += a
            right = b
            b, a = max(right, left), right
        return b