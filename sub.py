import paho.mqtt.client as mqtt                       
import cv2                                            
import json                                           
import numpy as np                                    
# This is the Subscriber                              
# hostname                                            
broker = "localhost"                              
# port                                                
port = 1883                                           
# time to live                                        
timelive = 60                                         
                                                      
                                                      
def on_connect(client, userdata, flags, rc):          
    print("Connected with result code "+str(rc))      
    client.subscribe("/data")                         
                                                      
                                                      
def on_message(client, userdata, msg):                
    dataImg = msg.payload.decode()                    
    data = json.loads(dataImg)                        
    img = np.array(data)                              
    cv2.imwrite('bendeptrai.png', img)                
    print(img.shape)                                  
                                                      
                                                      
client = mqtt.Client()                                
client.connect(broker, port, timelive)                
client.on_connect = on_connect                        
client.on_message = on_message                        
client.loop_forever()                                 
                                                      
                                                      
                                                      
