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


#problem 2239.Find Closest NUmber to Zero, Level : Easy

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        pos = []
        neg = []

        #splitting numbers into positive and negative
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        #if no negative numbers, return the smallest positive number        
        if not neg:
            return min(pos)

        #if no positive numbers, return the largest negative number
        elif not pos:
            return max(neg)

        else:
            a = min(pos)
            b = max(neg)
            
            #Return the number with minimum absolute value, largest number in case of tie
            return abs(a) if abs(a) == abs(b) else (b if abs(b) < abs(a) else a)

sol = Solution()
print(sol.findClosestNumber([-4,-3,1,4,6]))

