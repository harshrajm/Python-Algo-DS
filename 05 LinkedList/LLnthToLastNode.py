class Node:

    def __init__(self,value):
        self.value = value
        self.next =None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
   


def nth_to_last_node(num,head):
    
    current = head
    count = 0
    while current:
        count = count +1
        current = current.next
    print(f"-> {count}")
    
    curr1 = head
    for i in range(count):
        if(i == count-num):
            print(curr1.value)
        curr1 = curr1.next   

def nth_to_last_node_new(num,head):
    left = head
    right = head
    for i in range(num-1):
        right = right.next
    print(f"left {left.value} ; right {right.value}")    
    while True:
        if(right.next == None):
            print(f"ans in {left.value}")
            break
        right = right.next
        left = left.next
    
        
print("start")
nth_to_last_node_new(2,a)
nth_to_last_node_new(3,a)   