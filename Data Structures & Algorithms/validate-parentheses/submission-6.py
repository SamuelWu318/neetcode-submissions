class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        kv = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in kv:
                if stack and stack[-1] == kv[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
    
        return len(stack) == 0
            

