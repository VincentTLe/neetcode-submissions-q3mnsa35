class MinStack:

    def __init__(self):
        # Constructor
        # Create a list so it gonna store item like stack
        self.my_stack = []

    def push(self, val: int) -> None:
        # Push item in the list
        self.my_stack.append(val)

    def pop(self) -> None:  
        self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return min(self.my_stack)
