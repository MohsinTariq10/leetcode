class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
            for j in range(i+1, n):
                maxi = max(nums[i : j])
                mini = min(nums[i : j])
                s += (maxi - mini)
        return s