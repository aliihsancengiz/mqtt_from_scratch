import socket
import select
import mqttBroker
import yaml

def getConfig():
    server_addr=()
    with open('server_config.yaml') as f:
        data=yaml.safe_load(f)
        server_addr=(data['ip'],data['port'])
        f.close()
    return server_addr


server_addr=getConfig()


Broker=mqttBroker.Broker(server_addr)
Broker.run()


connected_list=[Broker.get_socket()]

while True:
    read_sockets,_,exception_sockets=select.select(connected_list,[],connected_list)
    
    for notified_socket in read_sockets:
        if notified_socket is Broker.get_socket():
            # New Connection
            client_sock,client_addr=Broker.get_socket().accept()
            print(f"{client_addr} is connected.")
            client_sock.setblocking(False)
            connected_list.append(client_sock)
        else:
            if notified_socket not in exception_sockets:
                frame=Broker.GetMqttFrame(notified_socket)
                if frame is None:
                    connected_list.remove(notified_socket)
                else:
                    Broker.process_frame(notified_socket,frame)
            else: 
                    connected_list.remove(notified_socket)
    print("Number of client",len(connected_list)-1)
   
