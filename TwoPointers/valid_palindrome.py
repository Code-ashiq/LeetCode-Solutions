# problem 125. Valid Palindrome, Level: Easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
         # Initialize two pointers
        L = 0
        R = len(s) -1

        # Loop until the pointers meet
        while L < R:
            # Skip non-alphanumeric characters from the left
            if not s[L].isalnum():
                L += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[R].isalnum():
                R -= 1
                continue
            
            # Compare characters in a case-insensitive manner
            if s[L].lower() != s[R].lower():
                return False
            
            # Move both pointers towards the center
            L += 1
            R -= 1
        
        # All characters matched; it's a valid palindrome
        return True
    
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))