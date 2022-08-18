class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.recur(nums, len(nums)-1, dp)
    
    def recur(self, nums, ind, dp):
        if ind < 0: return 0
        if ind == 0: return nums[ind]
        
        if dp[ind] == -1:
            pick = nums[ind] + self.recur(nums, ind-2, dp) 
            nopick = 0 + self.recur(nums, ind-1, dp)
            dp[ind] = max(pick, nopick)
        return dp[ind]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = nums[0]
        b = 0
        i = 1
        for i in range(1, n):
            pick = nums[i]
            if i -2 >= 0 : pick += b
            no_pick = a
            a, b = max(pick, no_pick), a
        return a