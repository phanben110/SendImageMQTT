# simulator device 1 for mqtt message publishing              
import paho.mqtt.client as paho                               
import time                                                   
import random                                                 
import json                                                   
import cv2                                                    
# hostname                                                    
broker = "20.204.100.76"                                      
# port                                                        
port = 1883                                                   
                                                              
                                                              
def on_publish(client, userdata, result):                     
    print("Device 1 : Data published.")                       
    pass                                                      
                                                              
                                                              
client = paho.Client("admin")                                 
client.on_publish = on_publish                                
client.connect(broker, port)                                  
count = 0                                                     
                                                              
while (1):                                                    
    img = cv2.imread("b.jpg")                                 
    frame = img.tolist()                                      
    imgJson = json.dumps(frame)                               
    #message = f"ben dep trai {count}"                        
    count += 1                                                
    print(count)                                              
    time.sleep(0.1)                                           
    # publish message                                         
    ret = client.publish("/data", imgJson)                    
                                                              
