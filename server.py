import socket
import threading
from database import databaseset, cratedatabase, newcell
import time

global starttime

def handle_client(client_socket):
    starttime = time.time()
    while True:
        if time.time() - starttime >= 60:
            print("Клиент отключён")
            break
        data = client_socket.recv(1024)
        if not data:
            break
        num, id = data.decode().split()
        print("Received from client: " + num + " id=" + id)

        databaseset(num, id)
#        if time.time() - starttime >= 60:
#            break
    client_socket.close()


host = "127.0.0.1"
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Server listening on", host, ":", port)

cratedatabase()
#createdatabase
bindid = 1

server.settimeout(10)
while True:
    try:
        client_socket, client_address = server.accept()
    except socket.timeout:
        print("Конец работы")
        break
    client_id = str(bindid)
    newcell(client_id)
    bindid += 1
    client_socket.send(client_id.encode())
    print("Accepted connection from:", client_address)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
server.close()

