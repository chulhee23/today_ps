class Stack:
    def __init__(self):
        self.top = []

    def __len__(self):
        return len(self.top)
    
    def __str__(self):
        return str(self.top[::1])

    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("stack underflow")
            exit()

    def isEmpty(self):
        return len(self.top) == 0

stack = Stack()
stack.push(2)
stack.push(1)
stack.push(3)
print(stack)
stack.pop()
print(stack)
