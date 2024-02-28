current_hours = input("Введите текущее время (часы): ")
current_minutes = input("Введите текущее время (минуты): ")

try:
    current_hours = int(current_hours)
    current_minutes = int(current_minutes)
except ValueError as error:
    print(error)
    exit()

if current_hours < 0 or current_hours > 23 or current_minutes < 0 or current_minutes > 59:
    print("Ошибка: Некорректно введено время.")
else:
    remaining_hours = 23 - current_hours
    remaining_minutes = 59 - current_minutes
    time_until_midnight = remaining_hours * 60 + remaining_minutes + 1 
    print("До следующего дня осталось:", time_until_midnight // 60, "часов и", time_until_midnight % 60, "минут.")


