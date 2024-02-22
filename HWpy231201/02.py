import calendar

weekdays = list(calendar.day_name)
current_day_index = 0
response = "OK"

while True:
    if response == "OK":
        print("День недели -", weekdays[current_day_index])
    response = input("Хотите увидеть следующий день? (Введите 'OK' для продолжения, или 'exit' для выхода): ")
    if response.lower() == 'exit':
        break
    current_day_index = (current_day_index + 1) % 7
