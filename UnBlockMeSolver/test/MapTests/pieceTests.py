from Map.Piece import Piece
from Map.Move import Move
import unittest

class TestPiece(unittest.TestCase):

	def test_init(self):
		# test for simple case where no exception is expected
		piece = Piece(0,0,False)
		self.assertEquals(piece.x, 0)
		self.assertEquals(piece.y, 0)
		self.assertEquals(piece.isVertical, False)

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

	def test_move(self):
		piece = Piece(0, 0, False)

		# test right move valid
		move  = Move.right('*')
		piece.move(move)
		self.assertEquals(piece.x, 1)
		self.assertEquals(piece.y, 0)

		# test left move valid
		move  = Move.left('*')
		piece.move(move)
		self.assertEquals(piece.x, 0)
		self.assertEquals(piece.y, 0)

		# test vertical move on horizontal piece
		move = Move.up('*')
		with self.assertRaises(AttributeError):
			piece.move(move)

		# test up move valid
		piece = Piece(0, 0, True)
		move  = Move.up('*')
		piece.move(move)
		self.assertEquals(piece.x, 0)
		self.assertEquals(piece.y, -1)

		# test down move valid
		move  = Move.down('*')
		piece.move(move)
		self.assertEquals(piece.x, 0)
		self.assertEquals(piece.y, 0)

		# test horizontal move on vertical piece
		move  = Move.right('*')
		with self.assertRaises(AttributeError):
			piece.move(move)

		# test invalid move given
		move.up = 3
		with self.assertRaises(AttributeError):
			piece.move(move)

		# test invalid type given
		move  = None
		with self.assertRaises(AttributeError):
			piece.move(move)

