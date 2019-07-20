import paho.mqtt.client as mqtt
#externalHosts
broker="40.81.27.10"
#mqtt_port
mqtt_port=1883
#mqtt_username
username="f456d95d-b76f-43e9-8b35-bac8383bf941:5366fbed-f8e4-4c8f-99ce-8faf6575dfe4"
password="y4aVpae5yi4Edjr00AQ6oG9NB"
def on_publish(client,userdata,result):             #create function for callback
    print("data published")
   
client= mqtt.Client()                           #create client object

client.username_pw_set(username,password)

client.on_publish = on_publish                          #assign function to callback
client.connect(broker,mqtt_port)                                 #establish connection
client.publish("/hello","hi!")    




