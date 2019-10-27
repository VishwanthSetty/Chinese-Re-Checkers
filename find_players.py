import socket

class Sock():
    def create_socket(self):
        sock = socket.socket()
        return sock

    def bind_socket(self, sock, host, port):
        sock.bind((host, port))

def receive_message():
    player_msg, player_addr = Socket.recvfrom(1024)
    if player_addr not in players:
        players.append(player_addr)

def send_message(msg):
    Socket.sendto(str.encode(msg), (server_host, server_port))

host = '127.0.0.1'
port = 5000

server_host = '127.0.0.1'
server_port = 80

sock = Sock()
Socket = sock.create_socket()
sock.bind_socket(Socket, host, port)

players = []

print("-->")
message = input()

while True:
    #if "Quit" not in message:
        #send_message(message)
    #receive_message()
    try:
        player_msg, player_addr = Socket.recvfrom(1024)
        if player_addr not in players:
            players.append(player_addr)
        print("--> Connected to: " + player_msg)
        message = input()

    except:
        pass