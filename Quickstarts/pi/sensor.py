
#========= CONNECTION STRING ===========================================================
CONNECTION_STRING = "<YOUR CONNECTION STRING HERE>"
#========================================================================================









import time
import sys
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

r = 255
g = 255
b = 255

sense.clear((r, g, b))
sleep(1)


PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000


MSG_TXT = "{\"temperature\": %.2f,\"humidity\": %.2f}"

def send_confirmation_callback(message, result, user_context):
    print ( "IoT Hub responded to message with status: %s" % (result) )

def iothub_client_init():
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
   
            temperature = sense.get_temperature()
            humidity = sense.get_humidity()
            msg_txt_formatted = MSG_TXT % (temperature, humidity)
            message = IoTHubMessage(msg_txt_formatted)

            prop_map = message.properties()
            if temperature > 30:
              prop_map.add("temperatureAlert", "true")
            else:
              prop_map.add("temperatureAlert", "false")
	
	
            print( "Sending message: %s" % message.get_string() )
            client.send_event_async(message, send_confirmation_callback, None)
	    sense.show_message(temperature + " C")
	    time.sleep(1)
	    sense.show_message(humidity + "%")
            time.sleep(2)

    except IoTHubError as iothub_error:
        print ( "Unexpected error %s from IoT Hub" % iothub_error )
        return
    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Sense HAT" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
