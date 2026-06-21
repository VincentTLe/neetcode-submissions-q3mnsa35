class Solution:
    def isValid(self, s: str) -> bool:
        # String consisting bracket:  (), [], {} 
        #  Open bracket is close by the same type of bracket
        # edge case : odd number length of string 
        valid = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for char in s:
            # If the character is opening bracket add in stack
            if char in "({[":
                stack.append(char)
            else: # If closing character then compare it to the last opening character ,  if not true return False
                # When the stack is  empty, and opening with close bracket:

                if stack and valid[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0
        
        
