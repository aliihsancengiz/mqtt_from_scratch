import mqtt_pb2

class MQTT_REQUEST:
    def make_publish_request(self,topic,message):
        frame=mqtt_pb2.mqtt_frame()
        frame.frame_type=mqtt_pb2.mqtt_frame.mqtt_request
        frame.request.method=mqtt_pb2.Request.pub_request
        frame.request.payload.topic=topic
        frame.request.payload.message=message   
        return frame
    
    def make_subscribe_request(self,topic):
        frame=mqtt_pb2.mqtt_frame()
        frame.frame_type=mqtt_pb2.mqtt_frame.mqtt_request
        frame.request.method=mqtt_pb2.Request.sub_request
        frame.request.payload.topic=topic
        return frame
    
    def make_unsubscribe_request(self,topic):
        frame=mqtt_pb2.mqtt_frame()
        frame.frame_type=mqtt_pb2.mqtt_frame.mqtt_request
        frame.request.method=mqtt_pb2.Request.unsub_request
        frame.request.payload.topic=topic
        return frame

class MQTT_RESPONSE:
    def make_ack_response(self):
        frame=mqtt_pb2.mqtt_frame()
        frame.frame_type=mqtt_pb2.mqtt_frame.mqtt_response
        frame.response.status=mqtt_pb2.Response.ACK
        return frame

    def make_nack_response(self):
        frame=mqtt_pb2.mqtt_frame()
        frame.frame_type=mqtt_pb2.mqtt_frame.mqtt_response
        frame.response.status=mqtt_pb2.Response.NACK
        return frame    


