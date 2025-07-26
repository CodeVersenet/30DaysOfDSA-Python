# Day04_binary_Search_Position.py
#  Binary Search Position
# LeetCode Problem: https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

#374. Guess Number Higher or Lower
# LeetCode Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1