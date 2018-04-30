class Game():
    def __init__(self):
        self.Actions = {}
        self.numActions = 0
        self.Value = None
        self.Goal = None
        self.MovesLeft = None
        self.TotalMoves = None

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

    def setMoves(self,value):
        self.MovesLeft = self.Moves = value

    def addMove(self,moveName,moveValue):
        self.numActions += 1
        if moveName == "Add":
            self.Actions[self.numActions] = (self.AddNum,moveValue)
        elif moveName == "Subtract":
            self.Actions[self.numActions] = (self.SubNum,moveValue)
        elif moveName == "Multiply":
            self.Actions[self.numActions] = (self.MultNum,moveValue)
        elif moveName == "Divide":
            self.Actions[self.numActions] = (self.DivNum,moveValue)

    def printMoves(self):
        print (self.Actions)

    def printGameState(self):
        print("Action dictionary", self.Actions)
        print("Number of moves left is: ", self.numActions)
        print("Current value is: ", self.Value)
        print("The goal is: ", self.Goal)
        print(self.Moves)

    def tryMoves(self,someArray):
        for i in someArray:
            self.printGameState()
            playable = self.Actions[i] #returns a tuple

            playable[0](playable[1]) #call that action with its assigned value, if any
            self.MovesLeft -= 1
            self.printGameState()