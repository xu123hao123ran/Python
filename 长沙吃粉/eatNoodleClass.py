class noodle:
    def __init__(self):
        self.type = None
        self.weight = 0
        self.ma = None

    def setType(self, type):
        self.type = type

    def setWeight(self, weight):
        self.weight = weight

    def setMa(self, ma):
        self.ma = ma

    def printV(self):
        print(f"type is {self.type}, weight is {self.weight}, ma is {self.ma}")


nood = noodle()
nood.setWeight(12)
nood.setType("大份")
nood.setMa("干的")
nood.printV()