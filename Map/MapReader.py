from Map import Map
import os

class MapReader(object):
	loaded     = False
	file_found = False

	def __init__(self):
		"""
		Initialize MapReader class
		"""
		super(MapReader, self).__init__()

	def load(self, file_name):
		"""
	    Set flags and test if the file given exists. Throws IOError
	    on file not existing.

		@type file_name: string
		@param file_name: Name of the file that contains definition of 
		                  the map.
	    """
		self.file_name  = file_name
		self.loaded     = False
		self.file_found = False

		if not os.path.exists(self.file_name):
			raise IOError(self.file_name + " not found.")
		else:
			self.file_found = True

	def get(self):
		"""
		Read the file and return the string inside

		@rtype:   string
		@return:  string inside of the specified file
		"""
		return open(self.file_name, 'r').read()