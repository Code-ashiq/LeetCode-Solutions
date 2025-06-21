#problem 2239.Find Closest Number to Zero, Level : Easy

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        pos = []
        neg = []

        #splitting numbers into positive and negative
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        #if no negative numbers, return the smallest positive number        
        if not neg:
            return min(pos)

        #if no positive numbers, return the largest negative number
        elif not pos:
            return max(neg)

        else:
            a = min(pos)
            b = max(neg)
            
            #Return the number with minimum absolute value, largest number in case of tie
            return abs(a) if abs(a) == abs(b) else (b if abs(b) < abs(a) else a)

sol = Solution()
print(sol.findClosestNumber([-4,-3,1,4,6]))