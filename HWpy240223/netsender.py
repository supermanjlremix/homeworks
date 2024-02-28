import socket

class Sender:
    
    def __init__(self, port):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message, dest_ip):
        data = message.encode('utf8')
        addr = (dest_ip, self.port)
        self.sock.sendto(data, addr)
        print(f'Отправлено к {addr} : {data}')

    