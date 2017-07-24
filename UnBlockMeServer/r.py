import requests

valid_map = "|||||\n" + \
	            "|000|\n" + \
	            "|**0$\n" + \
	            "|||||"
payload = {'graph': valid_map}
r = requests.post("http://localhost:8080", data=payload)
print r.status_code
print r.text


"""
Need to use body to send the map and then use the 
headers to send the delimter if required.
"""