class Queue2Stacks:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def size(self):
        return len(self.stack1)
    
    def isEmpty(self):
        return self.stack1 == []
        
    def enqueue(self,item):
        self.stack1.append(item)
        
    def dequeue(self):
        
        if(self.stack2 != []):
           return self.stack2.pop()
        else:
            if(self.stack1 == []):
                return "empty!!"
            else:
                for x in range(len(self.stack1)):
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        #return out
    
q =  Queue2Stacks()
q.enqueue("h")
q.enqueue("a")
q.enqueue("r")
q.enqueue("s")
q.enqueue("h")
print(q.size())
print(q.dequeue())
print(q.dequeue())
q.enqueue("r")
q.enqueue("a")
q.enqueue("j")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue()) 