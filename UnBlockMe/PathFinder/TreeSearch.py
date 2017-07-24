from PathFinder import PathFinder
from Utility.Stack import Stack
from Queue import Queue
from test import files
from Node import Node

class TreeSearch(PathFinder):

	def __init__(self, board, bfs=True):
		"""
		Initialize TreeSearch class.

		@type board:  Map
		@param board: Map to be solved
		@type bfs:    boolean
		@param bfs:   Whether this class will use breadth-first search or
		              depth-first search
		@rtype:       TreeSearch
		@return:      Initialized TreeSearch class
		"""
		super(TreeSearch, self).__init__(board)
		self.bfs = bfs

	def populateQueue(self, graph, move, queue, parent):
		"""
		Populate the queue with nodes and their cost.

		@type graph:   Map
		@param graph:  Graph to get moves from to populate queue
		@type move:    Move
		@param move:   Move to get to the 
		@type queue:   Queue
		@param queue:  Stack with nodes being added to it with the cost
		@type parent:  Node
		@param parent: Parent for the nodes that will be created
		"""
		# get possible moves
		moves = graph.getMoves()

		# create node
		node  = Node(graph, move, parent)

		# put into queue all the moves possible
		for move in moves:
			queue.put((move, node))

	def getPath(self):
		"""
		Get the best path to solve the given graph.

		@rtype:  [Move]
		@return: Array of moves which represent the path found to solve the puzzle
		"""

		if self.board.isSolved():
			return None

		# decide on the data structure to use which determines if breadth-first search
		# or depth-first search is being run. 
		queue = None
		if self.bfs == True:
			queue = Queue()
		else:
			queue = Stack()

		self.populateQueue(self.board, None, queue, None)
		discovered = {self.board.hash: True}

		while not queue.empty():
			move, node = queue.get()
			newBoard = node.graph.copyConfidentMove(move)

			if newBoard.hash not in discovered:
				if newBoard.isSolved():
					path = node.reconstructPath()
					path.append(move)
					return path

				discovered[newBoard.hash] = True
				self.populateQueue(newBoard, move, queue, node)

		return None

