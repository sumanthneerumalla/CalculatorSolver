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

    def setup(self):
        self.Goal = int(input("What is the goal number? "))
        self.setTotalMoves(int(input(" How many moves? ")))
        self.setStart(int(input("What number to start at? ")))
        done = False
        while not done:
        #Todo: revisit this in relation to the AddMove function, might need cleaning up.
            moveName = input("Enter the name of the move: ")
            value = input("Enter a value if any, n or nothing if it doesnt have one: ")
            if not value.isdigit():
                value = None
            else:
                value = int(value)
            self.addMove(moveName,value)
            done = input("Another move? Enter if yes, N to stop ")


    # mygame.addMove("Add", 2)
    # mygame.addMove("Add", 3)
    # mygame.printMoves()


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

    def DelNum(self,value):
        #dont really need the value arg but we keep it for now
        strVersion = str(self.Value)
        end = len(strVersion)
        self.Value = float(strVersion[:end-1]) #take out the last num and store again

    def NegNum(self,value):
        #do nothing with the value again
        self.Value = -self.Value

    def AppendNum(self,value):
        strVersion = str(self.Value)
        self.Value =  float(strVersion + str(value))

    def setStart(self,value):
        self.Value = self.Start = value

    def setGoal(self,value):
        self.Goal = value

    def setTotalMoves(self,value):
        self.MovesLeft = self.TotalMoves = value


    def addMove(self,moveName,moveValue = None):
        self.numActions += 1
        if moveName == "Add":
            self.Actions[self.numActions] = (self.AddNum,moveValue,"Add")
        elif moveName == "Sub":
            self.Actions[self.numActions] = (self.SubNum,moveValue, "Subtract")
        elif moveName == "Mul":
            self.Actions[self.numActions] = (self.MultNum,moveValue, "Multiply")
        elif moveName == "Div":
            self.Actions[self.numActions] = (self.DivNum,moveValue, "Divide")
        elif moveName == "Del":
            self.Actions[self.numActions] = (self.DelNum,moveValue,"Delete")
        elif moveName == "Neg":
            self.Actions[self.numActions] = (self.NegNum,moveValue,"Negate")
        elif moveName == "App":
            self.Actions[self.numActions] = (self.AppendNum,moveValue,"Append")

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
            #Todo: Change this to stop right after the game has been won, not until all moves are exhausted
            if(self.Value == self.Goal):
                print("Game won! Moves are: " + str(list(round)) )
                for i in round:
                    actionName =self.Actions[i][2]
                    actionValue = self.Actions[i][1]
                    if actionValue == None:
                        actionValue = ""
                    else:
                        actionValue = str(actionValue)

                    print(actionName + ": " + actionValue)
                break
            else:
                print("Tried: " + str(list(round)) + ", any key to try another game")

