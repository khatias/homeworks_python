class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)


    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None


    def is_empty(self):
        return len(self.stack) == 0




stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print(stack.pop()) 
print(stack.pop())  
print(stack.pop())  


print(stack.pop()) 
