from Map.Move import Move
from test import files
import unittest

class TestMove(unittest.TestCase):

	def test_init(self):
		# test all valid kinds of moves and if no exception is thrown
		# then the test case is passed
		move = Move('a',1,0)
		move = Move('a',-1,0)
		move = Move('a',0,1)
		move = Move('a',0,-1)

		# test all diagnols and make sure excpetion is thrown
		with self.assertRaises(AttributeError):
			move = Move('a',1,1)

		with self.assertRaises(AttributeError):
			move = Move('a',-1,1)

		with self.assertRaises(AttributeError):
			move = Move('a',1,-1)

		with self.assertRaises(AttributeError):
			move = Move('a',-1,-1)

		# test when a number too high and too low is given
		with self.assertRaises(AttributeError):
			move = Move('a',-3,0)

		with self.assertRaises(AttributeError):
			move = Move('a',0,3)

		# test when a type other than string is given to make sure
		# an exception is thrown
		with self.assertRaises(AttributeError):
			move = Move(0,-1,-1)

		with self.assertRaises(AttributeError):
			move = Move(['a'],-1,-1)

	def test_isValid(self):
		# test if a valid move is valid
		move = Move('a',0,1)
		self.assertTrue(move.isValid())

		# test if negative values are okay
		move.up    = -1
		self.assertTrue(move.isValid())

		move.right = -1
		move.up    = 0
		self.assertTrue(move.isValid())

		# test if invalid up is invalid
		move.up = 3
		self.assertFalse(move.isValid())

		# test if invalid right is invalid
		move.up    = 0
		move.right = -3
		self.assertFalse(move.isValid())

		# test if both invalid up and right is invalid
		move.up    = -3
		move.right = 3
		self.assertFalse(move.isValid())

		# test if diagnols are invalid
		move.up    = 1
		move.right = 1
		self.assertFalse(move.isValid())

		move.up    = -1
		move.right = 1
		self.assertFalse(move.isValid())

		move.up    = 1
		move.right = -1
		self.assertFalse(move.isValid())

		move.up    = -1
		move.right = -1
		self.assertFalse(move.isValid())

	def test_left(self):
		move = Move.left('a')
		self.assertEquals(move.piece, 'a')
		self.assertEquals(move.up, 0)
		self.assertEquals(move.right, -1)

	def test_right(self):
		move = Move.right('a')
		self.assertEquals(move.piece, 'a')
		self.assertEquals(move.up, 0)
		self.assertEquals(move.right, 1)

	def test_up(self):
		move = Move.up('a')
		self.assertEquals(move.piece, 'a')
		self.assertEquals(move.up, -1)
		self.assertEquals(move.right, 0)

	def test_down(self):
		move = Move.down('a')
		self.assertEquals(move.piece, 'a')
		self.assertEquals(move.up, 1)
		self.assertEquals(move.right, 0)
