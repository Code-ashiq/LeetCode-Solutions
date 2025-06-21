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