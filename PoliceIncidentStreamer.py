import requests
import csv
import time

#Make a request to get the data from the sensor
response = requests.get("http://data.chattlibrary.org/resource/bh2e-2vwv.json")
#print(response.json())
j = response.json()
i = 0
for incident in j:
	print i
	i += 1
	print incident
	requests.post("http://localhost:1337/PoliceIncidents/create?data="+str(incident))
	

# d =  j[1]
# print d
# data = requests.get("http://beehive1.mcs.anl.gov/api/1/nodes/0000001e061089e5/export?date="+d+"&version=2")
# decoded_content = data.content.decode('utf-8')
# cr = csv.reader(decoded_content.splitlines(), delimiter=',')
# reading = str(next(cr))

# time.sleep(14)
# #Send Data To Database
# requests.post("http://localhost:1337/AirSensor/create?data="+reading)


