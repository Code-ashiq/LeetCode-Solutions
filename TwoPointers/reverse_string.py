# problem 344. Reverse String, Level: Easy

class Solution:
    def reverseString(self, s: list[str]) -> str:
        left = 0
        right = len(s) -1

        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1


