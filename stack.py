class Stack:
    def __init__(self):
        self.stack:list

    def new_stack(self):
        self.stack = []

    def stack_empty(self):
        return len(self.stack) == 0
    
    def add_stack(self, value):
        self.stack.append(value)

    def delete_stack(self) :
        self.stack.pop()

    def __str__(self):
        return f"La liste est {self.stack}"