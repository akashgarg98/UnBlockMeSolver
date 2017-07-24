from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# import UnBlockMe Map and PathFinder. 
import sys
sys.path.append('../unBlockMe')
from Map.Map import Map
from PathFinder.TreeSearch import TreeSearch

# Constants keys for the user to use
MAP_KEY       = "graph"
DELIMETER_KEY = "delimeter"

# HTTP response codes
HTTP_SUCCESS     = 200
HTTP_BAD_REQUEST = 400

class Server(BaseHTTPRequestHandler):
	def _set_headers(self, response=HTTP_SUCCESS):
		"""
		Set headers for http response.
		"""
		self.send_response(response)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		"""
		Send pre-written HTML file to user.
		"""
		self._set_headers()
		f = open("index.html", "r")
		self.wfile.write(f.read())

	def do_HEAD(self):
		"""
		Default BaseHTTTPRequestHandler call to _set_headers()
		"""
		self._set_headers()

	def do_POST(self):
		"""
		Based on users response send 
		"""
		# initialize response variables
		response_code   = HTTP_BAD_REQUEST
		response_string = None

		# check if the map key was in the request
		if MAP_KEY not in self.headers:
			response_string = "Key " +  MAP_KEY + " not found"
		else:
			# initialize board
			board = None

			try:
				# check if delimeter given and initialize map
				if DELIMETER_KEY in self.headers:
					board = Map(self.headers[MAP_KEY], delimeter=self.headers[delimeter])
				else:
					board = Map(self.headers[MAP_KEY])

				# run pathfinding on the map
				ts = TreeSearch(board)
				response_string = ts.getPath()
				response_code = HTTP_SUCCESS
			except Exception as ex:
				# https://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occurred
				template = "An exception of type {0} occurred. Arguments:\n{1!r}"
				response_string = template.format(type(ex).__name__, ex.args)

		# send response to user
		self._set_headers(response=response_code)
		self.wfile.write(response_string)
		
def run(server_class=HTTPServer, handler_class=Server, port=8080):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print "Server running on port:", port
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()