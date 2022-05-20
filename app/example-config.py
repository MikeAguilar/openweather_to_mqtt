###
### ATTENTION READER !!!
### - Fill in all the variables below with your own information
### - Rename this file to config.py to ensure the app runs properly


# General Variables
device_name = "my_first_node"
freq = 120 # This number indicates how often (in seconds) the app will request OpenWeather API data and publish it.

# OpenWeather Information
api_key = "YOUR_API_HERE"
city = "Seattle"
units = "imperial"   # standard, metric or imperial

# MQTT Broker Information
mqtt_addr = "your.mqtt_broker.address"
mqtt_port = 1883
mqtt_user = "your-mqtt-user"
mqtt_pass = "your-mqtt-user-password"

# MQTT Publishing Details
topic_temp = "home/openweather-tracker/" + device_name.replace(" ", "") + "/" + city.replace(" ", "") + "/temperature"
topic_hum  = "home/openweather-tracker/" + device_name.replace(" ", "") + "/" + city.replace(" ", "") + "/humidity"
topic_pres = "home/openweather-tracker/" + device_name.replace(" ", "") + "/" + city.replace(" ", "") + "/pressure"

