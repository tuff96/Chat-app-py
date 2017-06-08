import sys
import socket
import threading

HOST=input('Give ip: ')
PORT=int(input('Give port'))
#HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
#PORT = 

def handle_client(sock, addr):
    while True:
        try:
            msg=sock.recv(4048)
            print(msg.decode())
            for s in SOCKET_LIST:
                #if(s!=sock):
                s.send(msg)
        except (ConnectionError, BrokenPipeError):
            print('Closed connection to {}'.format(addr))
            SOCKET_LIST.remove(sock)
            sock.close()
            break



def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    print ("Chat server started on port " + str(PORT))

    while True:
        # accept connections from outside
        (soc, address) = server_socket.accept()
        SOCKET_LIST.append(soc)
        thread = threading.Thread(target = handle_client, args = [soc, address], daemon=True)
        thread.start()
    s.close()

chat_server()
