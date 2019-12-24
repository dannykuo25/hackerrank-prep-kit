class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals: return 0
        result = 0
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr:
                result += 1
                curr = min(intervals[i][1], curr)
            else:
                curr = intervals[i][1]
        return result
