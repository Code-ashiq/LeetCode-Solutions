# Problem 771. Jewels and Stones, Level: Easy

#BRUTE FORCE METHOD

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
    
sol = Solution()
print(sol.numJewelsInStones("aAbB", "aAABB"))

#OPTIMAL SOLUTION USING SETS

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count