import CalculatorGameSolver

mygame = CalculatorGameSolver.Game()


mygame.setGoal(8)
mygame.setMoves(3)
mygame.setValue(0)
mygame.addMove("Add",2)
mygame.addMove("Add",3)
mygame.printMoves()
mygame.tryMoves([1,2])