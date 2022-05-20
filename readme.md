# OpenWeather API to MQTT
 Get OpenWeather API data and send it to MQTT Broker
#

## Brief

This is a Python application that runs from a Docker container. It gets weather information from the OpenWeather API (free key required) and will publish Temperature and Humidity individual messages to an MQTT Broker to be distributed and stored in a database (this is requires a separate Bridge to collect the MQTT messages and store them into an InfluxDB table).

## Features
- Collect current weather info from OpenWeather API
- Publish MQTT messages for Temperature, Humidity and Pressure

## Important files
- `./docker-compose.yml`

- `./dockerfile`

- `./requirements.txt`

- `./app/main.py`

- `./app/config.py` _(this file is listed  in the `.gitignore` file, so you need to rename the sample file provided)_

- `./app/example-config.py` _(rename this file to `config.py` once you have modified it with your own info)_ 

## Settings for `config.py`
### General Variables
- `device_name` = "my_first_node"
    </br> The device name needs to be alphanumeric and '_' or '-' only as it becomes part of the publishing topic.
- `freq` = 120 
    </br> This number indicates how often (in seconds) the app will request OpenWeather API data and publish it.

### OpenWeather Information
- `api_key` = "YOUR_API_KEY_HERE"
    </br> You can get a free API key from the OpenWeather API website.
- `city` = "Seattle"
    </br> This is the city that will be requested from the API. This name also becomes part of the publishing topic. The application will remove blank spaces from the City value to ensure the topic is valid.
- `units` = "imperial" 
    </br> These are the units that will be used in the response. They can be `standard`, `metric`, or `imperial`.

### MQTT Broker Information
- `mqtt_addr` = "your.mqtt_broker.address"
    </br> This is the IP or Hostname/FQDN for your MQTT Broker.
- `mqtt_port` = 1883
    </br> This is the Port for your MQTT Broker.
- `mqtt_user` = "your-mqtt-user"
    </br> This is the User for your MQTT Broker.
- `mqtt_pass` = "your-mqtt-user-password"
    </br> This is the Password for your MQTT Broker.

### MQTT Publishing Details
- `topic_temp` = "home/openweather-tracker/`device_name`/`city`/temperature"
- `topic_hum`  = "home/openweather-tracker/`device_name`/`city`/humidity"
- `topic_pres` = "home/openweather-tracker/`device_name`/`city`/pressure"
</br> Note that the topics will be populated by **default** as presented above. Only change them if absolutely necessary.

## How to run it
The `docker-compose` command will build the Docker image for you using the included `dockerfile`. 
- Download the project from Github to a machine with Docker and Docker Compose installed.

- Modify the `example-config.py` file with your own information and rename it to `config.py`

- From the CLI, change to the directory `openweather_to_mqtt`.

- **Start** the application with `docker-compose`
    ```
    docker-compose up -d --build
    ```
- **Stop** the application with `docker-compose`
    ```
    docker-compose down
    ```
