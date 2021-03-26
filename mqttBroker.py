import socket
import mqtt_pb2
import mqttIOService
import mqttPacketGenerator
import mqttHelpers
import mqttTopicRouter




class Broker(mqttIOService.ProtocolIO,mqttPacketGenerator.MQTT_REQUEST,mqttPacketGenerator.MQTT_RESPONSE):
    def __init__(self,server_addr):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        self.server_socket.bind(server_addr)
        self.router=mqttTopicRouter.TopicRouter()

    def run(self):
        self.server_socket.listen()
    
    def process_frame(self,endpoint,frame):
        if frame.frame_type is mqtt_pb2.mqtt_frame.mqtt_request:
            # Send Ack
            ack=self.make_ack_response()
            self.WriteMqttFrame(ack,endpoint)
           
            if frame.request.method is mqtt_pb2.Request.pub_request:
                t=frame.request.payload.topic
                m=frame.request.payload.message
                self.router.publish(t,m) 

            elif frame.request.method is mqtt_pb2.Request.sub_request:
                self.router.subscribe(endpoint,frame.request.payload.topic)
            
            elif frame.request.method is mqtt_pb2.Request.unsub_request:
                self.router.unsub(endpoint,frame.request.payload.topic)


        elif frame.frame_type is mqtt_pb2.mqtt_frame.mqtt_response:
            pass
        else:
            pass

    def get_socket(self):
        return self.server_socket


