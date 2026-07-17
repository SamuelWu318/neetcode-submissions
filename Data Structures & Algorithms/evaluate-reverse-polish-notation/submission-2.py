class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try: 
                int_token = int(token)
                stack.append(int_token)
            except: 
                if token == "+":
                    new = stack[-2] + stack[-1]
                elif token == "-":
                    new = stack[-2] - stack[-1]
                elif token == "*":
                    new = stack[-2] * stack[-1]
                elif token == "/":
                    new = int(stack[-2] / stack[-1])
                
                stack.pop()
                stack.pop()
                stack.append(new)
            
            print(stack)
        
        return stack[0]
        
            