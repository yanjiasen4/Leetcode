# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
def lcmp(x,y):
    return x.start < y.start

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        size = len(intervals)
        result = []
        if size <= 0: return result
        intervals.sort(key=lambda x:x.start)
        size = len(intervals)
        for i in range(0,size-1):
            if intervals[i].end >= intervals[i+1].start:
                intervals[i+1].start = intervals[i].start
                if intervals[i].end > intervals[i+1].end:
                    intervals[i+1].end = intervals[i].end
            else:
                result.append(intervals[i])
        result.append(intervals[size-1])
        return result