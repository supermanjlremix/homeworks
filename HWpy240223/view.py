import datetime

class View:

    def __init__(self, controller):
        self.controller = controller

    def show_message(self, name_from, message):
        name_from = name_from.title()
        dt = datetime.datetime.now()
        time = dt.strftime('%H:%M:%S')
        print(f"[{time}] {name_from}: {message}")

    def get_message(self):
        msg = input('>>> ')
        msg = msg.strip()
        self.controller.on_input(msg)


