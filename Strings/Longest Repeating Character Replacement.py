"""
LeetCode: Longest Repeating Character Replacement
Difficulty: Medium
Topic: String, sliding window, substrings.

Approach:
Maintain a dictionary of characters and their count.
size(window) - max(count of all characters) <= k
i.e there are only k attempts to replace characters in the window while max(count of characters) are the repeating chars.

Time: O(n)
Space: O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        CharCount = {}
        l = 0
        res = 0

        for r in range(len(s)):
            CharCount[s[r]] = CharCount.get(s[r],0) + 1

            if  (r + 1 - l) - max(CharCount.values()) > k:
                CharCount[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res