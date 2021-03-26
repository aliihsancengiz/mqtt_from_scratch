import mqttIOService
import mqttPacketGenerator



class TopicRouter:

    def __init__(self):
        self.topicListenerMap={}

    def subscribe(self,endpoint,topic):
        if topic not in self.topicListenerMap:
            self.topicListenerMap[topic]=[]
        self.topicListenerMap[topic].append(endpoint)
    def publish(self,topic,msg):
        if topic not in self.topicListenerMap:
            return None
        listener=self.topicListenerMap[topic]
        frame=mqttPacketGenerator.MQTT_REQUEST().make_publish_request(topic,msg)
        for s in listener:
            mqttIOService.ProtocolIO().WriteMqttFrame(frame,s)         
    
    def unsub(self,endpoint,topic):
        if endpoint in self.topicListenerMap[topic]:
            self.topicListenerMap[topic].remove(endpoint)


