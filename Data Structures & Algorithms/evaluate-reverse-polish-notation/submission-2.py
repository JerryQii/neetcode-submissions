class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ("+", "-", "*", "/"):
                parm2 = int(stack.pop())
                parm1 = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(parm1 + parm2)
                elif tokens[i] == "-":
                    stack.append(parm1 - parm2)
                elif tokens[i] == "*":
                    stack.append(parm1 * parm2)
                elif tokens[i] == "/":
                    stack.append(int(float(parm1) / parm2))
            else:
                stack.append(tokens[i])
        return int(stack[0])