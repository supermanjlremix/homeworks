from controller import Controller

print("Добро пожаловать в наш чат!\n\n")
app = Controller('contacts.json', 11488)
app.start()
