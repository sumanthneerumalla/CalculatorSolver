import itertools

class Game():
    def __init__(self):
        self.Actions = {}
        self.numActions = 0
        self.Start = None
        self.Value = None
        self.Goal = None
        self.MovesLeft = None
        self.TotalMoves = None

    def reset(self):
        self.Value = self.Start
        self.MovesLeft = self.TotalMoves

    def AddNum(self,value):
        self.Value += value

    def SubNum(self,value):
        self.Value -= value

    def MultNum(self,value):
        self.Value *= value

    def DivNum(self,value):
        self.Value /= value

    def setStart(self,value):
        self.Value = self.Start = value

    def setGoal(self,value):
        self.Goal = value

    def setMoves(self,value):
        self.MovesLeft = self.TotalMoves = value

    def addMove(self,moveName,moveValue):
        self.numActions += 1
        if moveName == "Add":
            self.Actions[self.numActions] = (self.AddNum,moveValue,"Add")
        elif moveName == "Subtract":
            self.Actions[self.numActions] = (self.SubNum,moveValue, "Subtract")
        elif moveName == "Multiply":
            self.Actions[self.numActions] = (self.MultNum,moveValue, "Multiply")
        elif moveName == "Divide":
            self.Actions[self.numActions] = (self.DivNum,moveValue, "Divide")

    def printMoves(self):
        print (self.Actions)

    def printGameState(self):
        print("Action dictionary", self.Actions)
        print("Total number of moves",self.TotalMoves)
        print("Number of moves left is: ", self.MovesLeft,"\n")
        print("The goal is: ", self.Goal)
        print("Current value is: ", self.Value,"\n")

    def generateMoves(self):
        allPlays = itertools.combinations_with_replacement(range(1,self.numActions+1),self.TotalMoves)
        return list(allPlays)


    def tryMoves(self,someTuple):
        for i in list(someTuple):
            self.printGameState()
            playable = self.Actions[i] #returns a tuple
            playable[0](playable[1]) #call that action with its assigned value, if any
            self.MovesLeft -= 1
            self.printGameState()


    def SolveGame(self):
        for round in itertools.combinations_with_replacement(range(1, self.numActions + 1), self.TotalMoves):
            self.reset()
            print("Before: \n")
            self.printGameState()
            self.tryMoves(round)
            print("After: \n")
            if(self.Value == self.Goal):
                print("Game won! Moves are: " + str(list(round)) )
                for i in round:
                    print( self.Actions[i][2] + ": " + str(self.Actions[i][1]) )
                break
            else:
                print("Tried: " + str(list(round)) + ", any key to try another game")

