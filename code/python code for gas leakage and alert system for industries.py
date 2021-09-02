import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "trfjpt",
        "typeId": "gas_alert_sensor",
        "deviceId":"trfipt"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    gas_level=random.randint(0,100)
    
    myData={'GAS_Level':gas_level}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()


 #api key: a-trfjpt-lzgnmt7vtj

 #authentication token: 0xTEY8&GWSY&52uR&U
