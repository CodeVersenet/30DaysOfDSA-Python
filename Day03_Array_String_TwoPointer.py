# Day 3 of #30DaysOfDSA #
# LeetCode Problem 283: Move Zeroes
class Solution:
    def moveZeroes(self, nums):
        non_zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1
        return nums

# Example usage
nums = [0, 1, 0, 3, 12]
sol = Solution()
result = sol.moveZeroes(nums)
print("After moving zeroes:", result)


#Problem 2: Implement strStr()

class StringSolution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

haystack = "leetcode"
needle = "code"
str_sol = StringSolution()
index = str_sol.strStr(haystack, needle)
print("First occurrence at index:", index)
