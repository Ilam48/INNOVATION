import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.connect("YOUR_DEVICE_API_ENDPOINT", 1883, 60)
client.loop_start()

iot_data = {
    "motion_detected": True,
    "temperature": 24
}

while True:
    client.publish("iot-2/evt/status/fmt/json", json.dumps(iot_data))
    time.sleep(5)
