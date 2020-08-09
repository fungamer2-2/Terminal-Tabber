# Documentation

Elements of system:
* `Tab(game)` : creates the Tab object that associates with the game it's inputted.

To make a tab, use the following syntax : `variable = Tab(game)`

Elements of built-in handwritten games:

* checkerboard: _This is a testing game._

Help:
Tab : class that has the following:

`Tab.__init__` : Initialize Tab.

`Tab.interact(inputCom)` : Interact with the game.

`Tab.resizegame(inh,inw)` : (input height, input width) Resize the game.

`Tab.fitintogame()` : Resize the tab into the game's w and h.

`Tab.fitgame()` : Resize the game into the tab's w and h.

`Tab.output()` : Make changes to the board.

`Tab.h` : Height

`Tab.w` : Width

`Tab.xpos` : X position of upper right corner.

`Tab.ypos` : Y position of upper right corner.

`resetBoard()` : Resets the board.

How to make a game to associate with the game:

1. Use `class` to begin.
2. Create a function inside the class named `__init__` with one parameter : `self`
3. Create `self.h` and `self.w` for width and height
4. Add a `inputCommand` function inside the class with two parameters : `self`,`inobj` (inobj stands for Input Object)
5. Put the following : 
```
def inputsize(self,inh,inw):
        self.h = inh
        self.w = inw
```
6. Make the class interact and change its variables.
7. Add a `output` function inside the class with one parameter : `self`
8. In the `output` function, make some calculations and return the board you want to output.
