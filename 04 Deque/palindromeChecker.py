class Deque:

    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insertFront(self,item):
        self.items.insert(0,item)

    def insertRear(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()


def palindromeChecker(str):

    d = Deque()

    for x in str:
        d.insertRear(x)


    while d.size() > 1:

        if(d.removeFront() != d.removeRear()):
            return False

    return True


print(palindromeChecker("lsdkjfskf"))
print(palindromeChecker("radar"))
