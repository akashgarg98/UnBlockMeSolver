from PathFinder import PathFinder
from Queue import Queue
from test import files
from Node import Node

class BFS(PathFinder):

	def populateQueue(self, graph, move, queue, parent):
		# get possible moves
		moves       = graph.getMoves()

		# create node
		node        = Node()
		node.graph  = graph
		node.parent = parent
		node.move   = move

		# put into queue all the moves possible
		for move in moves:
			queue.put((move, node))

	def getPath(self):
		if self.board.isSolved():
			return None

		queue = Queue()
		self.populateQueue(self.board, None, queue, None)
		discovered = {self.board.hash: True}

		while not queue.empty():
			move, node = queue.get()
			newBoard = node.graph.copyMove(move) # make a confident move once the bug is discovered

			if newBoard.hash not in discovered:
				if newBoard.isSolved():
					path = node.reconstructPath()
					path.append(move)
					return path

				discovered[newBoard.hash] = True
				self.populateQueue(newBoard, move, queue, node)

		return None

