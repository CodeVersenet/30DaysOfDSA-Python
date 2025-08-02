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

Concepts Covered:
-Binary Search (Iterative & Recursive)
-Time Complexity: O(log n)
-Edge Case Handling (start > end, duplicates)
-Left & Right Boundaries
-Search in Sorted Arrays

# Day 5 of #30DaysOfDSA – Keep Pushing Forward 
Problem 1: Best Time to Buy and Sell Stock

Problem 2: Valid Palindrome

#Concepts Covered:

-Sliding Window Technique
-Two Pointers
-String Preprocessing
-Edge Case Handling

#Problem Tags:
Arrays, Strings, Two-Pointers, Greedy

 # Day6 of #30DaysOfDSA - LeetCode Challenge 

#Problems Solved:
1. 69. Sqrt(x)  
2. 278. First Bad Version
##  Problem 1: [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
Key Concepts:

Binary Search
Math (Square Root Approximation)
Integer Overflow Handling
Time Complexity Optimization

Problem Tags:
-Binary Search
-Math
-Algorithm
-Easy

# Problem 2: 278. First Bad Version
#Problem Statement:
Given n versions [1, 2, ..., n] and an API isBadVersion(version), find the first bad version which causes all the following ones to be bad.
roblem 278: First Bad Version
 Link to problem [https://leetcode.com/problems/first-bad-version/submissions/1714841522/]

#Key Concepts:
Binary Search
API Interaction (Black Box Function)
Edge Case Handling
Search Space Reduction

#Problem Tags:
-Binary Search
-Interactive
-Easy

##  Day7 of #30DaysOfDSA - LeetCode Challenge 


Today, I focused on mastering **Linked List** problems by solving two fundamental challenges on LeetCode:
## Problem 1: [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### Key Concepts:
- Linked List Manipulation
- Iterative and Recursive Approach
- Pointers (prev, curr, next)

### Approach:
Reversed a singly linked list using both **iterative** and **recursive** methods. Focused on understanding pointer movement and memory references.

## Problem 2: [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

### Key Concepts:
- Linked List
- Floyd's Cycle Detection Algorithm (Tortoise and Hare)
- Fast and Slow Pointers

### Approach:
Used Floyd’s cycle detection technique to determine if a cycle exists in the linked list. This is a very efficient algorithm with **O(n)** time and **O(1)** space complexity.

## Tools Used:
- Language: **Python**
- Platform: **LeetCode**
- Editor: **VS Code**

## What I Learned:
- Mastery of basic linked list operations
- Understanding cycle detection in constant space
- Importance of pointer manipulation in interview-style problems


#  Day 8 - LeetCode Challenge

## Problem Solved:
**225. Implement Stack using Queues**  
[Link to problem](https://leetcode.com/problems/implement-stack-using-queues/)

## Problem Statement:
Implement a last-in-first-out (LIFO) stack using only two queues. You must use only standard operations of a queue.

---

## 💡 Key Concepts:
- Stack and Queue simulation
- Using Python `deque` for queue operations
- Push Costly method: reordering elements during push to maintain stack order
- Time Complexity:
  - Push: O(n)
  - Pop: O(1)
  - Top: O(1)
  - Empty: O(1)

---

##  Learning:
- Simulating one data structure using another sharpens logical thinking
- Importance of order manipulation to preserve behavior
- `deque` in Python is very flexible and efficient

## Code:
python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
   def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self) -> int:
        return self.q.popleft()
    def top(self) -> int:
        return self.q[0]
    def empty(self) -> bool:
        return not self.q

#  Day 9 of #30DaysOfDSA - LeetCode Challenge 


Today I solved two important array problems that are commonly asked in coding interviews.

#  Problem 1: [169. Majority Element](https://leetcode.com/problems/majority-element/)

###  Key Concepts:
- Frequency counting
- **Boyer–Moore Voting Algorithm**
- Greedy selection

###  Approach:
The Boyer-Moore algorithm finds the majority element in **O(n)** time and **O(1)** space by keeping track of a candidate and its count.

python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

#  Day 10 of #30DaysOfDSA - LeetCode Challenge 
# LeetCode 202 - Happy Number

## 📌 Problem Link:
[202. Happy Number](https://leetcode.com/problems/happy-number/)
## 📝 Problem Statement:
Write an algorithm to determine if a number is a **"happy number"**.

A happy number is defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay).
3. If it loops endlessly without reaching 1, then the number is not happy.
##  Key Concepts:
- **Mathematical Logic**
- **Cycle Detection using Hash Set**
- **Digit Manipulation**


##  Approach:
1. Use a `set()` to store previously seen numbers to detect cycles.
2. Continuously replace the number with the sum of the squares of its digits.
3. If the number becomes `1`, return `True`.
4. If the number repeats, return `False`.
5. 
## ⏱ Complexity Analysis:
- Time Complexity O(log n)per transformation (because digit count reduces per step)
-Space Complexity: O(log n) for storing seen numbers in a set.


Today I explored **set operations** and **mathematical logic** problems to strengthen my problem-solving versatility.

##  Problem 1: [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

###  Key Concepts:
- Set Operations (`intersection`)
- Removing Duplicates
- Python Set Efficiency

###  Approach:
1. Convert both input arrays into sets.
2. Use set intersection to find common elements.
3. Convert the resulting set back into a list.

###  Solution:
python
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
 
# 💻 Day 11 of #30DaysOfDSA - LeetCode Challenge

Today’s focus was on **sliding window techniques** and **two-pointer optimization**.  
Both problems are highly popular in coding interviews and helped reinforce advanced problem-solving skills.

##  Problem 1: [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

###  Key Concepts:
- Sliding Window
- Hash Map for character tracking
- Dynamic window resizing

###  Approach:
1. Maintain a **sliding window** to store the current substring without duplicates.
2. Use a dictionary to store the last seen index of characters.
3. If a duplicate is found, adjust the `left` pointer to skip past it.
4. Track the maximum substring length.

###  Solution:
python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = max_len = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len

