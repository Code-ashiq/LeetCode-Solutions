# Problem 20. Valid Parentheses, Level: Easy

class Solution:
    def isValid(self, s: str) -> bool:
         # Mapping of closing brackets to their corresponding opening brackets
        hashmap = {')': '(', ']': '[', '}': '{'}
        stk = [] # Stack to keep track of opening brackets

        for c in s:
            if c not in hashmap:
                # If character is an opening bracket, push to stack
                stk.append(c)
            else:
                # If stack is empty and we encounter a closing bracket, it's invalid
                if not stk:
                    return False
                else:
                    # Pop the last opening bracket from the stack
                    popped = stk.pop()
                    # If it doesn't match the expected opening bracket, it's invalid
                    if popped != hashmap[c]:
                        return False
                    
        # If stack is empty at the end, all brackets are matched correctly
        return not stk

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))