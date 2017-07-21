from Map.MapReader import MapReader
from test import files
import unittest

class TestReader(unittest.TestCase):

	def test_is_loaded(self):
		t1 = MapReader()
		t1.load(files.good)

		# test if we have loaded the file
		self.assertFalse(t1.loaded)

	def test_is_found(self):
		## test on valid file
		t1 = MapReader()
		t1.load(files.good)

		# test if we have loaded the file
		self.assertTrue(t1.file_found)

		## test on invalid file
		t2 = MapReader()

		# ioerror should be thrown
		with self.assertRaises(IOError):
			t2.load(files.not_real)

		# make sure that the file found flag is still false
		self.assertFalse(t2.file_found)

	def test_get(self):
		## test if the file found works
		t1 = MapReader()
		t1.load(files.sample)
		result = t1.get()

		# check type
		self.assertEquals(type(result), str)

		# check if string is valid
		self.assertTrue(result == "sample_string")

