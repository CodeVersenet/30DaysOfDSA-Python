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


## ✅ Problem 1: Remove Duplicates from Sorted Array  
-  [LeetCode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  
- Topic: Array, Two Pointers  

### Description:
Given a sorted array, remove the duplicates **in-place** such that each unique element appears only once and return the new length.

###  Python Solution:
```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

# Example
nums = [1, 1, 2, 2, 3]
sol = Solution()
k = sol.removeDuplicates(nums)
print("Unique count:", k)
print("Modified array:", nums[:k])

