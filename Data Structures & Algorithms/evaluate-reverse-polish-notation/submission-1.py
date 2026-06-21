import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input is a list with number and operators 
        # output is integer 
        # type cast division into integer 
        # if it's number save in the stack
        # pop the two peak elements to calculate
        stack = []  
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a,b : int(a/b)
                    }
        for i in tokens:
            if i in op_map:
                b = stack.pop()
                a = stack.pop()

                result = op_map[i](a,b)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()
