from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)

        for char in ransomNote:
            if hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
        return True
    
sol = Solution()
print(sol.canConstruct("aa", "aab"))