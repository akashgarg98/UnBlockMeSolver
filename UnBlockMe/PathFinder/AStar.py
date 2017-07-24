from PathFinder import PathFinder
from Queue import PriorityQueue
from AStarNode import AStarNode

class AStar(PathFinder):

	def populateQueue(self, graph, queue, parent):
		"""
		Populate the priority queue with nodes and their cost.

		@type graph:   Map
		@param graph:  Graph to get moves from to populate queue
		@type queue:   Queue
		@param queue:  Queue with nodes being added to it with the cost
		@type parent:  AStarNode
		@param parent: Parent for the nodes that will be created
		"""
		# get possible moves
		moves = graph.getMoves()

		# put into queue all the moves possible
		for move in moves:
			# make move and get copy
			newBoard = graph.copyConfidentMove(move)

			# calculate heuristic for this move that was made
			h = self.heuristic(newBoard)

			# create node
			node = AStarNode(newBoard, move, parent, parent.g + 1, h)

			# put the node in priority queue
			queue.put((node.cost(), node))

	def getPath(self, heuristic):
		"""
		Get the best path to solve the given graph.

		@rtype:  [Move]
		@return: Array of moves which represent the path found to solve the puzzle
		"""
		# make sure the board isn't already solved
		if self.board.isSolved():
			return None

		# make sure the given heuristic is a function that can be called
		if not callable(heuristic):
			return None
		self.heuristic = heuristic

		# initialize data structures for A*
		queue    = PriorityQueue()
		explored = {self.board.hash: True}

		# populate queue with moves and nodes
		self.populateQueue(self.board, queue, AStarNode(None, None, None, 0, 0))

		while not queue.empty():
			# get the next position from the queue
			cost, node = queue.get()

			# make sure this position hasn't been explored
			if node.graph.hash not in explored:
				# check if the board is solved
				if node.graph.isSolved():
					return node.reconstructPath()

				# if not solved, add to explored and populate queue
				explored[node.graph.hash] = True
				self.populateQueue(node.graph, queue, node)

		return None

