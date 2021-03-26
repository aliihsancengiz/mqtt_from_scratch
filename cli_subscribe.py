#!/usr/bin/python


import mqttIOService
import mqttPacketGenerator
import mqttHelpers
import socket
import argparse
import yaml

def getConfig():
    server_addr=()
    with open('server_config.yaml') as f:
        data=yaml.safe_load(f)
        server_addr=(data['ip'],data['port'])
        f.close()
    return server_addr


server_addr=getConfig()

client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sock.connect(server_addr)
client_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

req=mqttPacketGenerator.MQTT_REQUEST()
io=mqttIOService.ProtocolIO()

parser=argparse.ArgumentParser()
parser.add_argument("topic",help="topic to publish")

args=parser.parse_args()

frame=req.make_subscribe_request(args.topic)
io.WriteMqttFrame(frame,client_sock) 

while True:
    frame=io.GetMqttFrame(client_sock) 
    if frame is not None:
        mqttHelpers.printRequest(frame) 

client_sock.close()





