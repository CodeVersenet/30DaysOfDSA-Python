# Day05_Best_Time_To_Buy_And_Sell_Stock.py

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Example
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", maxProfit(prices))  # Output: 5


# Day05_Valid_Palindrome.py

def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Example
text = "A man, a plan, a canal: Panama"
print("Is Palindrome:", isPalindrome(text))  # Output: True
