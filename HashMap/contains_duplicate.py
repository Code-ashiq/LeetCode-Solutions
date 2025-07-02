# Problem 217. Contains Duplicate, Level: Easy

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Initialize an empty set to store unique elements
        s = set()
        for num in nums:
            if num in s:
                return True # Duplicate found, return True immediately
            else:
                # If not in the set, add the number to the set
                s.add(num)
        
        # If the loop completes with no duplicates, return False
        return False
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))