import os

class MapReader(object):
	loaded     = False
	file_found = False

	"""docstring for MapReader"""
	def __init__(self):
		super(MapReader, self).__init__()

	def load(self, file_name):
		"""
	    Return the x intercept of the line M{y=m*x+b}.  The X{x intercept}
	    of a line is the point at which it crosses the x axis (M{y=0}).
	    This function can be used in conjuction with L{z_transform} to
	    find an arbitrary function's zeros.
		@type m: number
		@param m: The slope of the line.
		@type b: number
		@param b: The y intercept of the line. The X{y intercept} of a
	              line is the point at which it crosses the y axis (M{x=0}).
	    @rtype:   number
	    @return:  the x intercept of the line M{y=m*x+b}.
	    """
		self.file_name  = file_name
		self.loaded     = False
		self.file_found = True

		if not os.path.exists(self.file_name):
			raise IOError(self.file_name + " not found.")
		else:
			self.file_found = True

	def get(self):
		print "to be implemented"
		
		