class Node(object):
	parent = None
	move   = None
	graph  = None

	def reconstructPath(self):
		"""
		Construct the path from here that it took to make it here.

		@rtype:  [Move]
		@return: array of moves to get to this point from the root node
		"""
		# initialize variables
		parent = self
		path   = [self.move]

		# loop through parents
		while parent != None:
			# add move to list and then change parent to next one
			if parent.move != None:
				path.append(parent.move)
				
			parent = parent.parent

		# reverse list and return result. Remove the first as it will be None
		return list(reversed(path[1:]))
		