class Game():
    def __init__(self):
        self.Actions = {}
        self.numMoves = 0
        self.Value = None
        self.Goal = None
        self.Moves = None

    def AddNum(self,value):
        self.Value += value

    def SubNum(self,value):
        self.Value -= value

    def MultNum(self,value):
        self.Value *= value

    def DivNum(self,value):
        self.Value /= value

    def setValue(self,value):
        self.Value = value

    def setGoal(self,value):
        self.Goal = value

    def setMove(self,value):
        self.Moves = value

    def addMove(self,moveName,moveValue):
        self.numMoves += 1
        if moveName == "Add":
            self.Actions[self.numMoves] = (self.AddNum,moveValue)
        elif moveName == "Subtract":
            self.Actions[self.numMoves] = (self.SubNum,moveValue)
        elif moveName == "Multiply":
            self.Actions[self.numMoves] = (self.MultNum,moveValue)
        elif moveName == "Divide":
            self.Actions[self.numMoves] = (self.DivNum,moveValue)

    def printMoves(self):
        print (self.Actions)
