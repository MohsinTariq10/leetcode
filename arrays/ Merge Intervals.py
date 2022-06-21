import numpy as np
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        non_overlap = []
        indices = []
        n = len(intervals)
        a = np.array(intervals)
        intervals = a[a[:, 0].argsort()].tolist()
        print(intervals)
        for interval in intervals:
            start, end = interval
            if not non_overlap:
                non_overlap.append(interval)
                continue
            s, e = non_overlap[-1]
            if start <= e:
                non_overlap[-1] = [min(start, s), max(end, e)]
            else:
                non_overlap.append(interval)
        return non_overlap