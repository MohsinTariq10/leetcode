import numpy as np
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort()
        while(i < len(intervals)-1):
            s1,e1 = intervals[i]
            s2, e2 = intervals[i+1]
            if(s2<=e1 and e2>=s1):
                intervals[i] = [min(s1,s2),max(e1,e2)]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals