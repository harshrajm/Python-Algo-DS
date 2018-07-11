class Node:

    def __init__(self,value):
        self.value = value
        self.next =None


def llReversal(head):
    a = head
    pointTo = None
    while (a != None):
        print(a.value)

        new  = Node(a.value)
        new.next = pointTo
        pointTo = new
        if(a.next == None):
            return new
        a = a.next



a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

def printll(head):
    x = head
    while(x != None):
        print(x.value)
        x = x.next

result = llReversal(a)
printll(result)

