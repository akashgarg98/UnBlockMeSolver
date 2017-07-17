from PathFinder.PathFinder import PathFinder
from Map.MapReader import MapReader
from PathFinder.bfs import BFS
from Map.Move import Move
from Map.Map import Map
from test import files
import unittest

class PathFindingTest(unittest.TestCase):

	def solve(self, board, moves):
		for move in moves:
			board.makeConfidentMove(move)

	def test_pathFinder(self):
		pf = PathFinder(None)

		with self.assertRaises(NotImplementedError):
			pf.getPath()
	
	def test_bfs(self):
		# test simple solve with one move
		mr     = MapReader()
		mr.load(files.quick_solve)
		tester = Map(mr)
		tester.setUp()
		bfs = BFS(tester)
		path = bfs.getPath()
		self.solve(tester, path)
		self.assertTrue(tester.isSolved())
		self.assertEquals(len(path), 1)

		# test simple solve with two moves
		mr     = MapReader()
		mr.load(files.right)
		tester = Map(mr)
		tester.setUp()
		bfs = BFS(tester)
		path = bfs.getPath()
		self.solve(tester, path)
		self.assertTrue(tester.isSolved())
		self.assertEquals(len(path), 2)

		# test simple solve with a few moves
		mr     = MapReader()
		mr.load(files.easy_solve)
		tester = Map(mr)
		tester.setUp()
		bfs = BFS(tester)
		path = bfs.getPath()
		self.solve(tester, path)
		self.assertTrue(tester.isSolved())
		self.assertEquals(len(path), 6)

		# test complex map
		mr     = MapReader()
		mr.load(files.simple_solve)
		tester = Map(mr)
		tester.setUp()
		bfs  = BFS(tester)
		path = bfs.getPath()
		self.solve(tester, path)
		self.assertTrue(tester.isSolved())
		self.assertEquals(len(path), 29)

		# test handing a solved map to bfs
		bfs  = BFS(tester)
		self.assertEquals(bfs.getPath(), None)

		# test impossible map
		mr     = MapReader()
		mr.load(files.impossible)
		tester = Map(mr)
		tester.setUp()
		bfs = BFS(tester)
		path = bfs.getPath()
		self.assertEquals(path, None)
