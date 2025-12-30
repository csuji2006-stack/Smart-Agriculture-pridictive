import time, json, random, math
import paho.mqtt.client as mqtt
from datetime import datetime

client = mqtt.Client()
client.connect("localhost", 1883, 60)

t = 0
while True:
    soil = int(50 + 20 * math.sin(t) + random.uniform(-5,5))
    temp = int(30 + 5 * math.cos(t) + random.uniform(-2,2))
    hum  = int(60 + 10 * math.sin(t/2) + random.uniform(-5,5))
    rain = random.choice([0,0,0,2,5])

    payload = {
        "timestamp": datetime.now().isoformat(),
        "soil_moisture": soil,
        "temperature": temp,
        "humidity": hum,
        "rainfall": rain
    }

    client.publish("farm/advanced", json.dumps(payload))
    print(payload)
    t += 0.1
    time.sleep(3)