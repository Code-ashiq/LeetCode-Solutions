#problem 1.Two Sum, Level : Easy

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)): # iterate over each element by index i
            for j in range(i+1, len(nums)): # iterate over elements after i
                if nums[i] + nums[j] == target: # check if sum equals target
                    return i,j #return the pair of indices

sol = Solution()
print(sol.twoSum([1,3,5,4],5))