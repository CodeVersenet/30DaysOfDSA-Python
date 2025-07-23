from typing import List
from functools import cache

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        @cache
        def dp(i, op1, op2):
            if i >= n:
                return 0
            s = dp(i+1, op1, op2) + nums[i]
            if op1 > 0:
                s = min(s, dp(i+1, op1-1, op2) + (nums[i] + 1) // 2)
            if op2 > 0 and nums[i] >= k:
                s = min(s, dp(i+1, op1, op2-1) + nums[i] - k)
            if op1 > 0 and op2 > 0 and (nums[i] + 1) // 2 >= k:
                s = min(s, dp(i+1, op1-1, op2-1) + (nums[i] + 1) // 2 - k)
            if op1 > 0 and op2 > 0 and nums[i] >= k:
                s = min(s, dp(i+1, op1-1, op2-1) + (nums[i] - k + 1) // 2)
            return s
        ans = dp(0, op1, op2)
        dp.cache_clear()
        return ans
        