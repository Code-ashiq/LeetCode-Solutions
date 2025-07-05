from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in the magazine
        hashmap = Counter(magazine)

        # Iterate over each character in the ransom note
        for char in ransomNote:
            # If the character is available in the magazine (count > 0), use one occurrence
            if hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                # If the character is not available, ransom note can't be constructed
                return False
        # All characters are available; ransom note can be constructed
        return True
    
sol = Solution()
print(sol.canConstruct("aa", "aab"))