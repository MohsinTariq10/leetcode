class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for j in range(n-1):
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = temp
                        