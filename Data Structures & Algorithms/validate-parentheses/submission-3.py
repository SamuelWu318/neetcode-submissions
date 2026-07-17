class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in {"{", "[", "("}:
                stack.append(s[i])
            elif len(stack) == 0:
                return False 
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop()
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

        return len(stack) == 0

