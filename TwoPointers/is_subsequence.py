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