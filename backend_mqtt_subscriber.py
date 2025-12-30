import json, sqlite3, paho.mqtt.client as mqtt

conn = sqlite3.connect("sensor.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sensor_data(
 timestamp TEXT,
 soil INTEGER,
 temperature INTEGER,
 humidity INTEGER,
 rainfall INTEGER
)
""")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        cur.execute("INSERT INTO sensor_data VALUES (?,?,?,?,?)",
                    (data["timestamp"], data["soil_moisture"],
                     data["temperature"], data["humidity"],
                     data["rainfall"]))
        conn.commit()
        print("Stored:", data)
    except:
        print("Invalid Data Ignored")

client = mqtt.Client()
client.connect("localhost",1883,60)
client.subscribe("farm/advanced")
client.on_message = on_message
client.loop_forever()