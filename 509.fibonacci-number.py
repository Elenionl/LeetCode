#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, N: int) -> int:
        if N in self.cache:
            return self.cache[N]
        result = self.fib(N - 1) + self.fib(N - 2)
        self.cache[N] = result
        return result


        
# @lc code=end

