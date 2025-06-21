# Problem 9.Palindrome number, Level : Easy

class Solution:
    def is_palindrome(self, x):
        x = str(x)
        return x == x[::-1]
    
if __name__ == "__main__": #Ensures that the code is run directly and not being imported
    sol = Solution()
    print(sol.is_palindrome(1211))