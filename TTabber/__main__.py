# unfinished
import os
import numpy
import math
from time import sleep

out_board = []

def resetBoard():
    global out_board
    out_board = []
    for x in range(40):
        out_board.append([])
        for y in range(40):
            out_board[x].append("_")

resetBoard()

# games

class checkerboard:
    def __init__(self):
        self.x = 40
        self.y = 40
    def inputCommand(self,inobj):
        self.x = inobj[0]
        self.y = inobj[1]
    def output(self):
        return (([["x","."] * round(self.x / 2)] + [[".","x"] * round(self.x / 2)]) * round(self.y / 2),self.x,self.y)

# systems

class Tab:
    def __init__(self,game):
        self.game = game()
        self.h = 30
        self.w = 30
        self.xpos = 0
        self.ypos = 0
    def interact(self,inputCom):
        self.game.inputCommand(inputCom)
    def output(self):
        (array_out,aaax,aaay) = self.game.output()
        for x in range(self.w):
            for y in range(self.h):
                out_board[x + self.xpos][y + self.ypos] = array_out[round(aaax / self.h * y)][round(aaay / self.w * x)]


while True:
    try:
        os.system('cls')
        for i in range(40):
            print(" ".join(out_board[i]))
        exec(input("-> "))
    except:
        pass
