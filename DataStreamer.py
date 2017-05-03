# import SimpleHTTPServer
# import SocketServer
import requests
import csv
import time

# PORT = 8000

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = SocketServer.TCPServer(("", PORT), Handler)

# print "serving at port", PORT
firstTime = True
lastData = 0
while True:
	#Make a request to get the data from the sensor
	response = requests.get("http://beehive1.mcs.anl.gov/api/1/nodes/0000001e061089e5/dates?version=2")
	#print(response.json())
	j = response.json()
	d =  j['data'][0]
	data = requests.get("http://beehive1.mcs.anl.gov/api/1/nodes/0000001e061089e5/export?date="+d+"&version=2")
	decoded_content = data.content.decode('utf-8')
	cr = csv.reader(decoded_content.splitlines(), delimiter=',')
	reading = str(next(cr))

	time.sleep(14)
	#Send Data To Database
	requests.post("http://localhost:1337/AirSensor/create?data="+reading)




