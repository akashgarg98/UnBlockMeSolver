# Unblock Me Repositiory

This repository aims to create a solver for puzzles found in applications like ```Unblock Me```. To do so it implements several solving methods including A\*, breadth first search, and depth first search. In addition a server will be implemented and hosted on heroku to provide a web service that users can call to solve their puzzles. 

## Structure

Packages have been separated into multiple directories each with their own tests.

* ```UnBlockMe``` that all packages will rely on. This has the map class which implements the game as well as the solvers implemented (A\*, BFS, and DFS).
* ```UnBlockMeServer``` implements a server that can be called to receive solutions for given boards. It will return moves or each board after the move has been made. Can be found on [heroku](https://unblockme.herokuapp.com/).
* ```UnBlockMeGame``` implements a GUI that allows users to build their own maps as well as play them. When ```UnBlockMeGenerator``` is finished it will use this library to create new games for the player everytime. (NOT IMPLEMENTED)
* ```UnBlockMeGenerator``` implements a toolset to generate maps that can be solved. (NOT IMPLEMENTED)
* ```UnBlockMeResearch``` is a meant as a workspace for looking into new ways to solve the puzzles. Specifically, initial work will be devoted to looking into admissable heuristics for A\*. The links below are initial start points for this work.
	* http://groups.csail.mit.edu/mac/users/bob/sliding-blocks.pdf
	* http://www.cs.princeton.edu/courses/archive/fall05/cos402/assignments/rushhour/index.html
	* https://geekoverdose.wordpress.com/2012/04/04/the-rushhour-puzzle-an-artificial-intelligence-toy-problem/
	* http://www.cs.huji.ac.il/~ai/projects/2015/RushHour/files/report.pdf
	* http://www.cs.cmu.edu/~ckingsf/class/02713-s13/lectures/lec11-astar.pdf
	* http://www.cs.huji.ac.il/~ai/projects/2012/RushHour/

## To Run

```make help``` provides the information for all the available commands.

## Future

Look into [performance](http://pyperformance.readthedocs.io/index.html) to see if benchmarks can be added in an interesting and useful way.
