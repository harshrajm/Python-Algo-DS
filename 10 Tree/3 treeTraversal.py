
#inorder
def inOrder(tree):
    if tree != None:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())
        
#preorder
def preOrder(tree):
    if tree != None:
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

#postorder
def postOrder(tree):
    if tree != None:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())