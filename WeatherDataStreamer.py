# import SimpleHTTPServer
# import SocketServer
import requests
import csv
import time

# while True:
#Make a request to get the data from the sensor
response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=4612862&APPID=ddd0bcdf88ded9f263f7c82c7072230a")
#print(response.json())
j = response.json()
print j

time.sleep(14)
#Send Data To Database
requests.post("http://localhost:1337/Weather/create?data="+reading)




