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



class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
    
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent = currentNode)
                
    def get(self,key):
        
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key > currentNode.key:
            return self._get(key,currentNode.rightChild)
        else:
            return self._get(key,currentNode.leftChild)


    def __setitem__(self, key, value):
        self.put(key,value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")


    def __delitem__(self, key):
        self.delete(key)

    def remove(self, nodeToRemove):
        #is Leaf
        if nodeToRemove.isLeaf():
            if nodeToRemove == nodeToRemove.parent.leftChild:
                nodeToRemove.parent.leftChild = None
            else:
                nodeToRemove.parent.rightChild = None
        #has 2 childs
        elif nodeToRemove.hasBothChildren():
            succ = nodeToRemove.findSuccessor()
            succ.splicOut()
            nodeToRemove.key  = succ.key
            nodeToRemove.val = succ.val
        #has one child
        else:
            if nodeToRemove.hasLeftChild():
                if nodeToRemove.isLeftChild():
                    nodeToRemove.leftChild.parent = nodeToRemove.parent
                    nodeToRemove.parent.leftChild = nodeToRemove.leftChild
                elif nodeToRemove.isRightChild():
                    nodeToRemove.leftChild.parent = nodeToRemove.parent
                    nodeToRemove.parent.rightChild = nodeToRemove.leftChild
                else:
                    nodeToRemove.replaceNodeData(nodeToRemove.leftChild.key,
                                                 nodeToRemove.leftChild.val,
                                                 nodeToRemove.leftChild.leftChild,
                                                 nodeToRemove.leftChild.rightChild)
            else:
                if nodeToRemove.isLeftChild():
                    nodeToRemove.rightChild.parent = nodeToRemove.parent
                    nodeToRemove.parent.leftChild = nodeToRemove.rightChild
                elif nodeToRemove.isRightChild():
                    nodeToRemove.rightChild.parent = nodeToRemove.parent
                    nodeToRemove.parent.rightChild = nodeToRemove.rightChild
                else:
                    nodeToRemove.replaceNodeData(nodeToRemove.rightChild.key,
                                                 nodeToRemove.rightChild.val,
                                                 nodeToRemove.rightChild.leftChild,
                                                 nodeToRemove.rightChild.rightChild)

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self.leftChild:
            yield from self.leftChild
        yield self
        if self.rightChild:
            yield from self.rightChild



b = BinarySearchTree()


b.put("1","one")
b.put("2","two")
b.put("3","three")

print(b.get("1"))
print(b.get("2"))
print(b.get("3"))
print(b.get("4"))

b.delete("2")
print(b.get("2"))
