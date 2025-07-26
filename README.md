# 30DaysOfDSA-Python
My 30-Day Python DSA Challenge journey with daily code, concepts, and solutions.


# Day 1 - Remove Duplicates from List
## Problem
Given a list of integers, remove all duplicates and return the unique elements sorted.
## Example
Input: [1, 2, 2, 3, 4, 1, 5]  
Output: [1, 2, 3, 4, 5]

## Concepts Covered
- Sets  
- Sorting  
- Python List Manipulation
Problem Name: Minimum Sum After Operations
LeetCode Link: https://leetcode.com/problems/minimum-sum-of-array-after-k-operations/
Concepts Used: Greedy Algorithm, Sorting, Heaps
Language: Python

# Day 2 of #30DaysOfDSA – Stack & String Manipulation

##  Problem 1: Valid Parentheses
- Platform: LeetCode
- Problem: Check if a string of brackets is valid (every opening bracket has a matching closing bracket in the correct order).
- Concepts Used: Stack, Hash Map (Dictionary)
- Difficulty: Easy

###  Key Learning:
- Use a stack to track open brackets.
- Use a dictionary to map closing brackets to their matching opening brackets.
- Return `True` only if the stack is empty at the end.


## Problem 2: Merge Two Sorted Lists
- Platform: LeetCode
- Problem: Merge two sorted linked lists and return it as a new sorted list.
- Concepts Used: Linked List, Two Pointer
- Difficulty: Easy

### Key Learning:
- Use a dummy node and iterate both lists.
- Append the smaller node each time and move the pointer.
- Handle edge cases when one list is empty.
  
# Day 3 - #30DaysOfDSA Challenge

Welcome to Day 3 of my #30DaysOfDSA challenge!  
Today, I practiced two classic problems involving Arrays and Strings using **Two Pointer** and **Sliding Window** techniques.


## Problem 1: Move Zeroes 
- Topic: Array, Two Pointers  

LeetCode #283

Topic: Array, Two Pointers

#Description:
Given an integer array nums, move all 0's to the end while maintaining the relative order of the non-zero elements. Do it in-place with O(1) extra space.

Python Solution:
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
#Output:
After moving zeroes: [1, 3, 12, 0, 0]

#Key Concepts:
Two Pointer Technique.
In-place array manipulation.
Preserves order of non-zero elements.


# Day 4 of #30DaysOfDSA
- Problem 1: Binary Search (LeetCode #704)
- Problem 2: Guess Number Higher or Lower (LeetCode #374)

Key Learning : Binary Search , Logarithmic Thinking, Edge Case Handling, Search in Sorted Arrays using Python 
#Key Concepts Covered:
-Binary Search (Iterative & Recursive)
-Time Complexity: O(log n)
-Edge Case Handling (start > end, duplicates)
-Left & Right Boundaries
-Search in Sorted Arrays

