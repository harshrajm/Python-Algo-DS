class Stack:

    def __init__(self):
        self.items = []
        
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items) - 1]
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
def isBalanced(str):
    
    if(len(str) % 2 != 0):
        return False
    
    open = "([{"
    close= ")]}"
    s = Stack()
    for x in str:
        if(x in open):
            
            s.push(x)
        if(x in close):
            if(s.isEmpty()):
                return False
            
            toCmp = s.pop()
            index1 = open.index(toCmp)
            index2 = close.index(x)
            if(index1 != index2):
                return False
           
            
    return s.size() == 0

            
a = "(({{}}))"
b = "[](){([[[]]])}"
c = "()(){]}"
d = "{{([][])}()}"
e = "[{()]"

print(isBalanced(a))
print(isBalanced(b))
print(isBalanced(c))
print(isBalanced(d))
print(isBalanced(e))
        
            
            
            
            
            