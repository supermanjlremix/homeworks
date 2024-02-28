import socket
import threading

class Listener:
    addr = ()
    sock = None
    running = False

    def __init__(self, port, controller):
        self.controller = controller
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        self.addr = (ip, port)
        self.sock.bind(self.addr)

    def worker(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
            except OSError:
                return
            message = data.decode('utf8')
            self.controller.on_message_received(message, addr[0])

    def start(self):
        self.running = True
        self.server = threading.Thread(target=self.worker)
        self.server.start()

    def stop(self):
        self.running = False
        self.sock.close() 
        self.server.join()
         

