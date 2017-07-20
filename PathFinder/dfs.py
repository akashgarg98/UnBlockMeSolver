from PathFinder import PathFinder
from Queue import Queue
from test import files
from Node import Node

class DFS(PathFinder):

	def populateQueue(self, graph, move, stack, parent):
		"""
		Populate the stack with nodes and their cost.

		@type graph:   Map
		@param graph:  Graph to get moves from to populate queue
		@type move:    Move
		@param move:   Move to get to the 
		@type stack:   [Node]
		@param stack:  Stack with nodes being added to it with the cost
		@type parent:  Node
		@param parent: Parent for the nodes that will be created
		"""
		# get possible moves
		moves = graph.getMoves()

		# create node
		node  = Node(graph, move, parent)

		# put into stack all the moves possible
		for move in moves:
			stack.append((move, node))

	def getPath(self):
		"""
		Get the best path to solve the given graph.

		@rtype:  [Move]
		@return: Array of moves which represent the path found to solve the puzzle
		"""
		if self.board.isSolved():
			return None

		stack = []
		self.populateQueue(self.board, None, stack, None)
		discovered = {self.board.hash: True}

		while len(stack) != 0:
			move, node = stack.pop()
			newBoard = node.graph.copyConfidentMove(move)

			if newBoard.hash not in discovered:
				if newBoard.isSolved():
					path = node.reconstructPath()
					path.append(move)
					return path

				discovered[newBoard.hash] = True
				self.populateQueue(newBoard, move, stack, node)

		return None

