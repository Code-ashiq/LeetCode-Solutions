# Problem 217. Contains Duplicate, Level: Easy

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))