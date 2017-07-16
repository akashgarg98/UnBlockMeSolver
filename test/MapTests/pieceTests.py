from Map.Piece import Piece
import unittest

class TestPiece(unittest.TestCase):

	def test_init(self):
		# test for simple case where no exception is expected
		piece = Piece(0,0,False)

		# test for cases where incorrect values are given
		with self.assertRaises(AttributeError):
			piece = Piece('0',0,False)

		with self.assertRaises(AttributeError):
			piece = Piece(0,'0',False)

		with self.assertRaises(AttributeError):
			piece = Piece(0,0,'False')

		# double check and make all wrong
		with self.assertRaises(AttributeError):
			piece = Piece('0','0','False')