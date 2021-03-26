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
parser.add_argument("message",help="message to publish")

args=parser.parse_args()


frame=req.make_publish_request(args.topic,args.message)
io.WriteMqttFrame(frame,client_sock)


client_sock.close()
