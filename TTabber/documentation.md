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

`Tab.output()` : Make changes to the board.

`Tab.h` : Height

`Tab.w` : Width

`Tab.xpos` : X position of upper right corner.

`Tab.ypos` : Y position of upper right corner.

`resetBoard()` : Resets the board.

How to make a game to associate with the game:

1. Use `class` to begin.
2. Create a function inside the class named `__init__` with one parameter : `self`
3. Create `self.x` and `self.y` for width and height ( I know, it's confusing )
4. Add a `inputCommand` function inside the class with two parameters : `self`,`inobj` (inobj stands for Input Object)
5. Make the class interact and change its variables.
6. Add a `output` function inside the class with one parameter : `self`
7. In the `output` function, make some calculations and return the board you want to output.
