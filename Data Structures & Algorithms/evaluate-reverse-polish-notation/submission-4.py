class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try: 
                int_token = int(token)
                stack.append(int_token)
            except: 
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    stack.append(-stack.pop() + stack.pop())
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                elif token == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
        
        return stack[0]
        
            