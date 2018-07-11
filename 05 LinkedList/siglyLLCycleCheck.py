class Node:

    def __init__(self,value):
        self.value = value
        self.next = None



def hasLoop(head):

    if (head == None):
        return False
    a = head
    b = head.next
    while (b != None):
        if(a == b):
            return True

        a = a.next
        b = b.next.next
    return False



a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print (hasLoop(a))



a1 = Node(1)
b1 = Node(2)
c1 = Node(3)
a1.next = b1
b1.next = c1
c1.next = a1

print (hasLoop(a1))
