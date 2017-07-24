import unittest
import requests
import copy

class TestMap(unittest.TestCase):

	valid_map = "|||||\n" + \
	            "|000|\n" + \
	            "|**0$\n" + \
	            "|||||"

	def test_valid_map(self):
		payload = {'graph': "asdf"}
		r = requests.post("http://localhost:8080", data=payload)
		print r

	def test_invalid_map(self):
		# empty

		# bad columns

		# regular string
		pass

	def test_delimeter(self):
		# test with good delimeter

		# test with bad delimeter
		pass

	def test_output_moves(self):
		pass

	def test_output_graphs(self):
		pass


if __name__ == '__main__':
	unittest.main()