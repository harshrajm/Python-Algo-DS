class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.disatnce = 0
        self.pred = None
        self.color = "white"

    def addNeighbour(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setDistance(self,dist):
        self.disatnce = dist

    def setPred(self,pred):
        self.pred = pred

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.disatnce

    def __str__(self):
        return str(self.id)+" connected to "+str([x.id for x in self.connectedTo])

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.length() > 0):
        currVertex = vertQueue.dequeue()
        for nbr in currVertex.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("grey")
                nbr.setDistance(currVertex.getDistance()+1)
                nbr.setPred(currVertex)
                vertQueue.enqueue(nbr)


