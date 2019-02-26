import sys
import iothub_service_client
from iothub_service_client import IoTHubDeviceMethod, IoTHubError
from builtins import input


CONNECTION_STRING = "{Your IoT hub service connection string}"
DEVICE_ID = "RaspberryPi"


METHOD_NAME = "SetTelemetryInterval"
METHOD_PAYLOAD = "10"
TIMEOUT = 60

def iothub_devicemethod_sample_run():
    try:
        iothub_device_method = IoTHubDeviceMethod(CONNECTION_STRING)

        response = iothub_device_method.invoke(DEVICE_ID, METHOD_NAME, METHOD_PAYLOAD, TIMEOUT)

        print ( "" )
        print ( "Device Method called" )
        print ( "Device Method name       : {0}".format(METHOD_NAME) )
        print ( "Device Method payload    : {0}".format(METHOD_PAYLOAD) )
        print ( "" )
        print ( "Response status          : {0}".format(response.status) )
        print ( "Response payload         : {0}".format(response.payload) )

        input("Press Enter to continue...\n")

    except IoTHubError as iothub_error:
        print ( "" )
        print ( "Unexpected error {0}".format(iothub_error) )
        return
    except KeyboardInterrupt:
        print ( "" )
        print ( "IoTHubDeviceMethod sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Python quickstart #2..." )
    print ( "    Connection string = {0}".format(CONNECTION_STRING) )
    print ( "    Device ID         = {0}".format(DEVICE_ID) )

    iothub_devicemethod_sample_run()
