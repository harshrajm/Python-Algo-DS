class DoublyLinkedList:

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)



a.next = b
b.prev = a
b.next = c
c.prev = b


print(a.value)
print(a.next.value)
print(a.next.next.value)
print(a.next.next.next)

print(c.value)
print (c.prev.value)
print (c.prev.prev.value)
print (c.prev.prev.next.next.value)
