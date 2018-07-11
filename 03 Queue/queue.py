class Queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    
q = Queue()    
print(q.isEmpty())    
q.enqueue(234)
q.enqueue("df")
q.enqueue(12.10)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())