"""
LeetCode: Valid Parentheses
Difficulty: Easy
Topic: String, Stack.

Approach:
push all the opening paranthesis. use a hashtable to find the opening paranthesis for the closing ones and pop them from stack.

Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")" : '(',
            ']' : '[',
            '}' :'{'}

        stack = []
        
        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False