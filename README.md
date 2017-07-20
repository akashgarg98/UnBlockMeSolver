# Unblock Me Solver

This repository aims to create a solver for puzzles found in applications like ```Unblock Me```. To do so it implements several solving methods including A\*, breadth first search, and depth first search. In addition a server will be implemented and hosted on heroku to provide a web service that users can call to solve their puzzles. 

Auto generated documentation:

* [Documentation](https://bi3mer.github.io/UnBlockMe/documentation/api.pdf) generated with [epydoc](http://epydoc.sourceforge.net/).
* [Code coverage](https://bi3mer.github.io/UnBlockMe/coverage/index.html) generated with [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/).

## To Run

```make help``` provides the information for all the available commands.

## A*

A* is implemented and tested, however, the given heuristic, [manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry), is an inadmissable heuristic and fails; this results in an inoptimal path. The distance metric would serve as an admissable heuristic if the game allowed for only single-step moves instead of multi-step moves. 

## To Delete

```python
def printDouble(self, string):
	split = string.split('\n')

	string = ""
	for row in split:
		row_string = ""
		for char in row:
			row_string += char + char

		string += row_string + "\n" + row_string + "\n"

	print string
```