# problem 228. Summary Ranges, Level : Easy

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0 # Initialize pointer to traverse the nums list

        while i < len(nums):
            start = nums[i] # Mark the start of a potential range

            # Continue moving pointer while numbers are consecutive
            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1

            # Check if we found a range (more than one number)
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i])) # Add range to answer
            else:
                ans.append(str(nums[i])) # Add single number to number

            i += 1 # Move to next number to start new range check

        return ans

sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))
print(sol.summaryRanges([0,2,3,4,6,8,9]))