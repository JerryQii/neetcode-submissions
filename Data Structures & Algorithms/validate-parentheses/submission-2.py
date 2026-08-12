class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap = {")":"(","}":"{","]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] in ("(","{","["):
                stack.append(s[i])
            else:
                if len(stack) > 0 and stack[len(stack)-1] == bracketmap[s[i]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0