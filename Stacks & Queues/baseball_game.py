class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = []

        for op in operations:
            if op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))

        return sum(stk)

sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(["1","C"]))  