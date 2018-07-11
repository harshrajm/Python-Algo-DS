class BinaryTree(object):
    
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
                        
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    def __str__(obj) :
        return f"[root {obj.key} - left {obj.leftChild} - right {obj.rightChild}]"
   
bt = BinaryTree('a')

print(bt)
bt.insertRight(4)
bt.insertLeft(5)
x = bt.getLeftChild()
x.insertLeft(666)
x.insertRight(777)
y = bt.getRightChild()
y.insertLeft(111)
y.insertRight(222)
print(bt)


def inOrder(tree):
    if tree != None:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())

def preOrder(tree):
    if tree != None:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())
 
        
def postOrder(tree):
    if tree != None:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())         
        
postOrder(bt)        