class HashTable(object):
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        
        hashValue = self.hashFunc(key,len(self.slots))
        
        if self.slots[hashValue] == None:  
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                newHash = reHash(hashValue,len(self.slots))
                while self.slots[newHash] != None and self.slots[newHash] != key:
                    newHash = self.reHash(newHash,len(self.slots))
                
                if self.slots[newHash] == None:
                    self.slots[newHash] = key
                    self.data[newHash] = data
                else:
                    self.data[newHash] = data
                    
                    
    def get(self,key):
        startHash = self.hashFunc(key,len(self.slots))
        
        position = startHash
        
        while self.slots[position] != None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.reHash(position,len(self.slots))
                if position == startHash:
                    return None
        
        
        
    def hashFunc(self,key,size):
        return key%size
    
    def reHash(self,oldHash,size):
        return (oldHash+1)%size
    
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