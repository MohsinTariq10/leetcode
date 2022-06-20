class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count = -1
        end = m
        for i in range(n):
            todo = nums2[i]
            while count != len(nums1):
                count +=1
                if nums1[count] ==0 and count>= end:
                    nums1[count] = todo
                    break
                
                if todo <= nums1[count]:
                    nums1.pop(-1)
                    nums1.insert(count, todo)
                    end +=1
                    break