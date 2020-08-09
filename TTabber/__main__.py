# unfinished
import os
import numpy
import math
from time import sleep

out_board = []

def resetBoard(): # does someone have a faster way to do this?
    global out_board
    out_board = []
    for x in range(40):
        out_board.append([])
        for y in range(40):
            out_board[x].append("_")

resetBoard()

# games

class checkerboard: # 😅 testing
    def __init__(self):
        self.h = 40
        self.w = 40
        self.one = "x"
        self.zero = "."
    def inputsize(self,inh,inw):
        self.h = inh
        self.w = inw
    def inputCommand(self,inobj):
        self.one = inobj[0]
        self.zero = inobj[1]
    def output(self):
        return (([[self.one,self.zero] * round(self.h / 2)] + [[self.zero,self.one] * round(self.h / 2)]) * round(self.w / 2),self.h,self.w)

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
    def resizegame(self,inh,inw):
        self.game.inputsize(inh,inw)
    def fitintogame(self):
        (self.h,self.w) = (self.game.h,self.game.w)
    def fitgame(self):
        self.resizegame(self.h,self.w)
    def output(self):
        (array_out,aaax,aaay) = self.game.output()
        for x in range(self.w):
            for y in range(self.h):
                out_board[x + self.xpos][y + self.ypos] = array_out[round(aaax / self.h * y)][round(aaay / self.w * x)]

if __name__ == "__main__":
    while True:
        try:
            os.system('cls')
            for i in range(40):
                print(" ".join(out_board[i]))
            exec(input("-> "))
        except:
            pass
