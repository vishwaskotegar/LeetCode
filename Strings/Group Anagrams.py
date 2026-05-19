"""
LeetCode: Group Anagrams
Difficulty: Medium
Topic: String, HashMap, string, sorting.

Approach:
create a hashmap as KEY = keeping count of letters and values = all matching anagrams.
OR
KEY = sorted string O(m.nlogn)

Time: O(26.m.n)
Space: O(26.n.m)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]):
        res = defaultdict(list)

        for s in strs: 
            count = [0] * 26

            for c in s: 
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return list(res.values())