class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()


def hotPotato(list,num):

    q = Queue()
    for x in list:
        q.enqueue(x)

    while q.size()>1:

        for z in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()
    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))