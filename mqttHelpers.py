import mqtt_pb2

def printRequest(frame):
    print("---------------------------------------------------------")
    if frame.frame_type is mqtt_pb2.mqtt_frame.mqtt_request:
        print("Frame Type : REQUEST")
        if frame.request.method is mqtt_pb2.Request.pub_request:
            print("Method Type : PUBLISH")
        elif frame.request.method is mqtt_pb2.Request.sub_request:
            print("METHOD Type : SUBSCRIBE")
        elif frame.request.method is mqtt_pb2.Request.unsub_request:
            print("METHOD Type : UNSUBSCRIBE")

        print("Topic : ",frame.request.payload.topic)
        if frame.request.payload.HasField("message"):
            print(frame.request.payload.message)
    else:
        print("Frame Type : RESPONSE")
        if frame.response.status is mqtt_pb2.Response.ACK:
            print("Status : ACK")
        else:
            print("Status : NACK")

    print("---------------------------------------------------------")


