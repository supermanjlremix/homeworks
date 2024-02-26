import socket

class UDP_Client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.client_socket.sendto(message.encode("utf8"), (self.server_address, self.server_port))

    def receive(self):
        data, addr = self.client_socket.recvfrom(1024)
        return data.decode()

    def close(self):
        self.client_socket.close()


