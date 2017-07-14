class Map(object):

	def __init__(self, graph, delimeter='\n'):
		"""
		Initialize the Map class and set the graph by either getting a
		a string from either a map reader or string as the graph 
		and breaking if not valid.

		@type graph:  string | MapReader
		@param graph: Represents the board that the game will be played on
		@type delimeter:  string
		@param delimeter: how to split the string
		"""
		super(Map, self).__init__()

		# if the type is not a string
		if type(graph) != str:
			# get the string from the reader
			graph = graph.get()

		# if the type of graph is not string anymore than something
		# should be thrown here
		if type(graph) != str:
			print "update this to throw a more useful error type"
			raise IOError("Incorrect type given to Map class")

		# split the string by the delimeter to create the graph
		self.graph = graph.split(delimeter)

	def isValid(self):
		"""
		Test if the graph in the map class is valid or not

		@rtype:  boolean
		@returN: graph is valid or not
		"""
		print "update this in the future"
		return True
		