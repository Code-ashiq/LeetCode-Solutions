# problem 977. Squares of a Sorted Array, Level: Easy

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
         # Initialize two pointers
        left= 0
        right = len(nums) -1
        result = []

        # Traverse the list from both ends
        while left <= right:
            # Compare the absolute values at both ends
            if abs(nums[left]) > abs(nums[right]):
                # Square the larger absolute value and add to result
                result.append(nums[left] **2)
                left += 1  # Move left pointer forward
            else:
                result.append(nums[right] **2)
                right -= 1  # Move right pointer forward

        # The result is in reverse order, so reverse it    
        result.reverse()

        return result

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
print(sol.sortedSquares([-7,-3,2,3,11]))

