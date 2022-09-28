


class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self,item):
        self.stack.append(item)
        return True 

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]
    
    def all_item(self):
        for i in self.stack:
            print(i)

stack = Stack()
stack.push(7)
stack.push(47)
stack.push(41)
stack.push(58)
stack.push(65)
print(stack.pop())


    
