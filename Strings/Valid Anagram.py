"""
LeetCode: Longest Repeating Character Replacement
Difficulty: Easy
Topic: String.

Approach:
Count the number of characters and make sure they are equal in both strings.

Time: O(n) : O(S+T)
Space: O(n) : Creating Hashmaps for both 
"""

"""Cheating"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # type: ignore
    """or"""
        return sorted(s) == sorted(t) # type: ignore
    #O(nLogn) for sorting 
    
"""Actual implementation"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
        for i in countS:
            if countS[i] != countT.get(i,0):
                
                return False
        return True