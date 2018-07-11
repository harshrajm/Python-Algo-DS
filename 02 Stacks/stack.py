


class Stack:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    
s = Stack()
print(s.isEmpty())
s.push(20)
print(s.isEmpty())
s.push('harshraj')
s.push(1258)
print(s.peek())
print(s.size())
s.pop()
s.pop()
s.pop()
print(s.isEmpty())
print(s.size())