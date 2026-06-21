class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input is a list with number and operators 
        # output is integer 
        # type cast division into integer 
        # if it's number save in the stack
        # pop the two peak elements to calculate
        stack = []  

        for i in tokens:
            if i not in "+-*/": 
                stack.append(int(i))
            else: 
                b = stack.pop()
                a = stack.pop()

                if i == "+": 
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack.pop()
