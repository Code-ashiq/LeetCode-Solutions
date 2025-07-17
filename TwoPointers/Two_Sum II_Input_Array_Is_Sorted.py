class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        n = len(numbers)
        r = n - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return (l+1, r+1)
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([2,3,4], 6))
print(sol.twoSum([-1,0], -1))