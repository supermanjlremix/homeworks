from netlistener import Listener
from netsender import Sender
from database import Database
from view import View

class Controller:
    listener : Listener
    sender : Sender
    db : Database
    view: View

    def __init__(self, filename, port) -> None:
        self.view = View(self)
        self.db = Database(filename)
        self.sender = Sender(port)
        self.listener = Listener(port, self)
    
    def start(self):
        self.listener.start()
        self.view.get_message()

    def stop(self):
        self.listener.stop()

    def on_message_received(self, message, ip):
        name = self.db.get_name(ip)
        if name:
            self.view.show_message(name, message)

    def on_input(self, message):
        if message:
            if message[0] == "@":
                try:
                    name, message = message.split(" ", 1)
                except ValueError:
                    pass
                else:
                    name = name[1:]
                    self.send_personal(name, message)
            else:
                self.send_broadcast(message)
        self.view.get_message()

    def send_personal(self, name, message):
        ip = self.db.get_ip(name)
        if ip is None:
            return
        self.sender.send(message, ip)

    def send_broadcast(self, message):
        names = self.db.get_all_names()
        for name in names:
            self.send_personal(name, message)


if __name__ == '__main__':
    import time
    test = Controller('contacts.json', 11488)
    test.start()
    time.sleep(0.1)
    test.sender.send('This is test message!', '192.168.110.106')
    time.sleep(3)
    test.stop()
