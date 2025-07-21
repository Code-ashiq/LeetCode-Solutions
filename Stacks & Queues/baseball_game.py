class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = [] # Stack to keep track of valid scores

        for op in operations:
            if op == "+":
                 # "+" means sum of last two valid scores
                stk.append(stk[-1] + stk[-2])
            elif op == "D":
                # "D" means double the last valid score
                stk.append(stk[-1] * 2)
            elif op == "C":
                # "C" means remove the last valid score
                stk.pop()
            else:
                # Otherwise, it's a valid integer score
                stk.append(int(op))

        return sum(stk)  # Return total score

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(["1","C"]))  