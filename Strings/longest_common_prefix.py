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