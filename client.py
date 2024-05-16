import socket
import random
import time

host = "127.0.0.1"
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

data = client.recv(1024)
id = data.decode()

starttime = time.time()
while True:
    if time.time() - starttime >= 15:
            print("Клиент отключился")
            break
    else:
        random_number = random.randint(1, 10)
        message = str(random_number) + " " + id
        client.send(str(message).encode())
        print("Sent:", random_number)
        time.sleep(3)
client.close()
