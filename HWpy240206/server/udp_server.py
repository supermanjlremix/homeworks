import socket

class UDP_Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(('localhost', self.port))

    def start(self):
        print(f"Сервер UDP начал прослушивание порта {self.port}")
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode()
            print(f"Получено сообщение от {addr}: {message}")
            self.server_socket.sendto("OK".encode("utf8"), addr)

    def stop(self):
        self.server_socket.close()


