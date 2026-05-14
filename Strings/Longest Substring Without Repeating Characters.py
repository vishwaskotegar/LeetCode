"""
LeetCode: Longest Substring Without Repeating Characters
Difficulty: Easy
Topic: String, Set

Approach:
Check if each character already exists in the set and remove left most character.
add new character to the set and calculate the current max.

Time: O(n)
Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CharSet = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in CharSet: 
                CharSet.remove(s[l])
                l += 1
            CharSet.add(s[r])
            res = max(res, r + 1- l)
        
        return res