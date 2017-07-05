import Map
from Map.mapReader import MapReader
import unittest

class TestReader(unittest.TestCase):

	real_file = "Reader/example_map.map"
	bad_file  = "Reader/doesnt_exist.map"

	def test_is_loaded(self):
		t1 = MapReader()
		t1.load(self.real_file)

		# test if we have loaded the file
		self.assertFalse(t1.loaded)

	def test_is_found(self):
		## test on valid file
		t1 = MapReader()
		t1.load(self.real_file)

		# test if we have loaded the file
		self.assertTrue(t1.file_found)

		## test on invalid file
		t2 = MapReader()

		# ioerror should be thrown
		with self.assertRaises(IOError):
			t2.load(self.bad_file)

if __name__ == '__main__':
    unittest.main()