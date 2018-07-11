class HashTable(object):
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        hashValue = self.hashfunction(key,len(self.slots))
        
        if self.slots[hashValue] == None :
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.reHash(hashValue,len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.reHash(nextSlot,len(self.slots))
                    
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data
        
    def hashfunction(self,key,size):
        #actual hash function
        return key%size
    
    def reHash(self,oldHash,size):
        return (oldHash+1)%size
    
    def get(self,key):
        
        startSlot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot
        
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.reHash(position,len(self.slots))
                if position == startSlot:
                    stop = True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)
        
        
h = HashTable(5)
h[1] = "harsh"
h[2] = "raj"
h[3] = "mahesh"
print(h[1])
print(h[2])
print(h[3])
h.put(3,"qwerty")
print(h[1])
print(h[2])
print(h[3])