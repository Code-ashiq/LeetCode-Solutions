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