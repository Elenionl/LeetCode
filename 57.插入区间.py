#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        index = 0
        output = []
        while index < len(intervals) and intervals[index][0] < new_start:
            output.append(intervals[index])
            index += 1
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)
        while index < len(intervals):
            interval = intervals[index]
            start, end = interval
            index += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output

# @lc code=end

