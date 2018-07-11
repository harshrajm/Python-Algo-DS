class TreeNode:
    
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return self.parent == None
    
    def isLeaf(self):
        return self.leftChild == None and self.rightChild == None
    
    def hasAnyChildren(self):
        return self.leftChild != None or self.rightChild != None
    
    def hasBothChildren(self):
        return self.leftChild != None and self.rightChild != None
    
    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.vaue = value
        self.rightChild = rc
        self.leftChild = lc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
    
tn = TreeNode(1,100,99)
print(tn.hasRightChild())
print(tn.isRoot())
print(tn.hasLeftChild())
print(tn.isLeaf())
print(tn.hasAnyChildren())
print(tn.hasBothChildren())