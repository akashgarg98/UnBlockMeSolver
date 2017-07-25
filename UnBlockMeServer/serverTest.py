import unittest
import requests
import copy

class TestMap(unittest.TestCase):

	valid_map = "|||||," + \
			    "|000|," + \
			    "|**0$," + \
			    "|||||"

	valid_payload = {"graph": valid_map, "delimeter": ","}

	def test_valid_map(self):
		r = requests.post("http://localhost:8080", headers=self.valid_payload)
		self.assertEquals(r.status_code, 200)
		self.assertEquals(r.text, '*, 2, 0')

	def test_invalid_map(self):
		# empty
		r = requests.post("http://localhost:8080", {})
		self.assertEquals(r.status_code, 400)
		r = requests.post("http://localhost:8080", {"graph":""})
		self.assertEquals(r.status_code, 400)
		r = requests.post("http://localhost:8080", {"graph":1})
		self.assertEquals(r.status_code, 400)

		# bad columns
		r = requests.post("http://localhost:8080", {"graph":"|||,|00|,|||", "delimeter":","})
		self.assertEquals(r.status_code, 400)

		# regular string
		r = requests.post("http://localhost:8080", {"graph":"asfasdf",})
		self.assertEquals(r.status_code, 400)

	def test_delimeter(self):
		# test with bad delimeter
		payload = {"graph": self.valid_map, "delimeter": "a"}
		r = requests.post("http://localhost:8080", headers=payload)
		self.assertEquals(r.status_code, 400)

	def test_output_graphs(self):
		payload = {"graph": self.valid_map, "delimeter": ",", "graphOutput": True}
		r = requests.post("http://localhost:8080", headers=payload)
		self.assertEquals(r.status_code, 200)
		complete = self.valid_map + "\n" + "|||||," + \
			                               "|000|," + \
			                               "|00**," + \
			                               "|||||"
		self.assertEquals(r.text, complete)

if __name__ == '__main__':
	unittest.main()