#problem 242.Valid Anagram, Level : Easy

from collections import Counter

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        # If lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

         # Count frequency of each character in both strings
        s_dict = Counter(s)
        t_dict = Counter(t)

         # Return True if both dictionaries are equal (i.e., same characters with same frequency)
        return s_dict == t_dict

sol = Solution()
print(Solution.isAnagram("anagram", "nagaram"))