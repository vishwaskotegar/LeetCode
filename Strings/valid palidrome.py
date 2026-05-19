"""
LeetCode: Valid palindrome
Difficulty: Easy
Topic: String.

Approach:
Use isalnum and reverse the string to compare.[::-1]

Time: O(n)
Space: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ''

        for c in s:
            if c.isalnum():
                formatted += c.lower()
        print(formatted)
        return formatted == formatted[::-1]