import socket

class Sock():
    def create_socket(self):
        Sock = socket.socket()
        return Sock

    def bind_socket(self):
        Socket.bind((host, port))

stop = False

host = '127.0.0.1'
port = 80

sock = Sock()
Socket = sock.create_socket()
sock.bind_socket()

players = []

while not stop:
    try:
        message, addr = Socket.recvfrom(1024)
        if "Quit" in message:
            stop = True

        print(str(message, "utf-8"))

    except:
        pass