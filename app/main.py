import string
import config

import paho.mqtt.client as mqttClient
import time
import requests
import json

### Connect to MQTT Broker and Publish the info
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False   #global variable for the state of the connection
 
broker_address= config.mqtt_addr
port = config.mqtt_port
user = config.mqtt_user
password = config.mqtt_pass
 
client = mqttClient.Client("OpenWeather-Tracker")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:

        ### Make the HTTP GET request to the API
        api_key=config.api_key
        city_name=config.city
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&units=" + config.units + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":

            y = x["main"]
            current_temperature = y["temp"]
            current_humidity    = y["humidity"]
            current_pressure    = y["pressure"]

            z = x["weather"]
            weather_description = z[0]["description"]
 
        temperature = current_temperature 
        humidity = current_humidity    
        pressure = current_pressure
        
        ### Publish results to MQTT Broker
        client.publish(config.topic_temp, str(temperature))
        client.publish(config.topic_hum, str(humidity))
        client.publish(config.topic_pres, str(pressure))
        
        print ("[+] Published | Temperature: {}, Humidity: {}, Pressure: {}".format(temperature, humidity, pressure))
        print ("[*] Sleeping for {} seconds...".format(config.freq) )
        time.sleep(config.freq) # This number establishes how frequent the code will run

except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()