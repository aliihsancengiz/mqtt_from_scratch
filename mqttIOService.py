import mqtt_pb2

HEADER_LENGTH=10


class ProtocolIO:
    def __init__(self):
        pass
    def WriteMqttFrame(self,frame,endpoint):
        obj_str=frame.SerializeToString()
        hdr=f"{len(obj_str):<{HEADER_LENGTH}}".encode("utf-8")
        msg=hdr+obj_str
        endpoint.send(msg)

    def GetMqttFrame(self,endpoint):
        try:
            hdr=endpoint.recv(HEADER_LENGTH).decode("utf-8").strip()
            if not hdr:
                return None
            message_len=int(hdr)
            msg=endpoint.recv(message_len)
            frame=mqtt_pb2.mqtt_frame()
            frame.ParseFromString(msg)
            return frame
        except:
            return None

