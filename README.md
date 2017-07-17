# Unblock Me Solver

This repository aims to create a solver for puzzles found in applications like ```Unblock Me```. To do so it implements several solving methods including A\*, breadth first search, and depth first search. In addition a server will be implemented and hosted on heroku to provide a web service that users can call to solve their puzzles. 

## To Run

```make help``` provides the information for all the available commands.

** Please note this repository is a work in progress and documentation and code will be updated in the near future **

## TO Fix

moves should actually allow for multiple spaces to be taken rather than just one.

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