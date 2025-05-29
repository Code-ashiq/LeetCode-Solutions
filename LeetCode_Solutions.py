# Problem 9.Palindrome number, Level : Easy

class Solution:
    def is_palindrome(self, x):
        x = str(x)
        return x == x[::-1]
    
if __name__ == "__main__": #Ensures that the code is run directly and not being imported
    sol = Solution()
    print(sol.is_palindrome(1211))

# Problem 13. Roman to Integer, Level : Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result + roman[s[-1]] #adding the last value

sol = Solution()
print(sol.romanToInt("XXV"))