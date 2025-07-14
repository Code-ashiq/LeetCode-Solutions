# problem 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left= 0
        right = len(nums) -1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] **2)
                left += 1
            else:
                result.append(nums[right] **2)
                right -= 1
            
        result.reverse()

        return result

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
print(sol.sortedSquares([-7,-3,2,3,11]))

