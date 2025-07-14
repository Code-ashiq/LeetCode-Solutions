# problem 344. Reverse String, Level: Easy

class Solution:
    def reverseString(self, s: list[str]) -> str:
         # Initialize two pointers
        left = 0
        right = len(s) -1

        # Loop until the two pointers meet or cross
        while left < right:
            # Swap the characters at left and right positions
            s[left],s[right] = s[right],s[left]
            
            # Move the left pointer forward and the right pointer backward
            left += 1
            right -= 1


