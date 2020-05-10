#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def calculate(nums1, s1, e1, nums2, s2, e2, k):
            if e1 < s1:
                return nums2[k + s2]
            if e2 < s2:
                return nums1[k + s1]
            if k < 1:
                return
# @lc code=end

