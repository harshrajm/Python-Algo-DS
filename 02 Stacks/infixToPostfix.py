class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def infixToPostfix(str):

    prec = "-+*/"
    s = Stack()
    postfix = ""
    for x in str:
        if(x in prec):
            print(f"in symbol {x}")
            if(s.isEmpty()):
                s.push(x)
            else:
                while(True):

                    if(s.peek() == "("):
                        s.push(x)
                        break
                    if(prec.index(s.peek()) > prec.index(x)):
                        postfix += s.pop()
                        s.push(x)
                        break
                    else:
                        s.push(x)
                        break
                        
        elif x == "(":
            s.push(x)
        elif x == ")":
            while(True):
                pop = s.pop()
                if(pop == "("):
                    break
                else:
                    postfix += pop
        else:
            print(f"in else {x}")
            postfix += x

    print(f"stack {s.items}")
    print(f"postfix {postfix}")

    while not s.isEmpty():
        postfix += s.pop()
    print(f"result = {postfix}")

infixToPostfix("x*y+z")
infixToPostfix("x+y")
infixToPostfix("x+(y*z)")
infixToPostfix("(A+B)*(C+D)")
infixToPostfix("(A+B)*C")