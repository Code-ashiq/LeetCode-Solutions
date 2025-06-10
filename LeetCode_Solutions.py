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


#problem 1.Two Sum, Level : Easy

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)): # iterate over each element by index i
            for j in range(i+1, len(nums)): # iterate over elements after i
                if nums[i] + nums[j] == target: # check if sum equals target
                    return i,j #return the pair of indices

sol = Solution()
print(sol.twoSum([1,3,5,4],5))


#problem 1768.Merge Strings Alternatively, Level : Easy

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = [] #list to store result
        i,j = 0,0 # initialize two pointers
        
        #loop till both pointers reach the end
        while i < len(word1) or j < len(word2): 

            # if characters left in word1, append to result and move pointer
            if i < len(word1):
                result.append(word1[i])
                i += 1

            # if characters left in word2, append to result and move pointer
            if j < len(word2):
                result.append(word2[j])
                j += 1

        # convert list of characters into string using join() 
        return "".join(result)

sol = Solution()
print(sol.mergeAlternately("ah","siq"))

#problem 392.Is Subsequence, Level : Easy 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        if s == '': return True  # if s is an empty string, it's always a subsequence
        if S > T: return False  #if s is longer  t, it can't be a subsequence

        j = 0 #pointer for string s
        
        # loop through each character in t
        for i in range(T):
            # if the current character in t matches the current character in s
            if t[i] == s[j]:
                # if we matched the last character in s, return True
                if j == S-1:
                    return True
                # move the next character in s
                j += 1
        # if loop completes without matching all the characters, return false
        return False
sol = Solution()
print(sol.isSubsequence("ace", "abcde"))


# problem 121.Best Time to Buy and Sell Stock, Level : Easy

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1  # initialize two pointers: l is buy, r is sell
        max_profit = 0 # variable to store the maximum profit found
        
        # Loop until r pointer reaches the end of the list
        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] # calculate the profit
                max_profit = max(max_profit, profit) # update max_profit if the profit is higher
            else:
                # if the price at r is less than or equal to price at l
                # it means a better buying opportunity, so move l to r
                l = r
            r += 1 # always move the right pointer forward
        return max_profit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))


# problem 14. Longest Common Prefix, Level : Easy

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""  # empty string to store the common prefix
        
        # Sort the list of strings lexicographically(that means dictionary order)
        # after sorting, the first and last strings will be the most different
        strs = sorted(strs)

        # Take the first and last strings in the sorted list
        first = strs[0]
        last = strs[-1]

        # compare characters of the first and last strings
        for i in range(min(len(first), len(last))):
            # if characters don't match, return the prefix found so far
            if(first[i] != last[i]):
                return ans
            # if characters match, add to the answer
            ans += first[i]

        # if loop completes, return the full common prefix
        return ans

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))


# problem 228. Summary Ranges, Level : Easy

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans

sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))
print(sol.summaryRanges([0,2,3,4,6,8,9]))
