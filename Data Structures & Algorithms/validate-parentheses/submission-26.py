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
            else:
                # NGẮN GỌN Ở ĐÂY: Nếu stack rỗng HOẶC dấu mở ở đỉnh không khớp cặp -> False luôn
                if not stack or stack[-1]!= valid[char]:
                    return False
                stack.pop()
        return len(stack) == 0
        
        
