
class BinHeap:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def insert(self,data):
        
        self.heapList.append(data)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percUp(self,i):   
        while i//2 >0:
            if self.heapList[i//2] > self.heapList[i]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i = i // 2
            
    def delMin(self):
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        retval = self.heapList.pop()
        self.percDown(1)
        return retval
    
    def percDown(self,i):
        while i*2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc    
            
    def minChild(self,i):
        if i * 2 +1 > self.currentSize:
            return i *2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
            
    def buildHeap(self,alist):
       i = len(alist)//2
       self.currentSize = len(alist)
       self.heapList = [0] + alist[:]
       while(i>0):
           self.percDown(i)
           i -= 1 

bh = BinHeap() 
bh.insert(1)
bh.insert(12)
bh.insert(13)
bh.insert(11)
bh.insert(14)
bh.insert(15)
bh.delMin()
bh.insert(122)
bh.insert(6)
print(bh.heapList)
            