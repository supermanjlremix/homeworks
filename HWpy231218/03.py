def show_time(hours, minutes="00", seconds="00"):
    #VN: зачем строковые     ^^^^ значения ^^^^ ? почему не просто 0?
    try:
        hours = int(hours) 
        minutes = int(minutes) 
        seconds = int(seconds) 
    except ValueError:
        print("Вы неправильно ввели количество чч:мм:сс")
        exit()

    #VN: ^^^ здесь те же замечания, что и к предыдущим задачам
    
    if seconds // 60 != 0:
        minutes += seconds // 60
        seconds = seconds % 60

    if minutes // 60 != 0:
        hours += minutes // 60
        minutes = minutes % 60

    hours = hours % 24

    text = 'Время: "%02d:%02d:%02d"'
    #VN:    ^^^^^^^^ это лишнее


    time = text % (abs(hours), abs(minutes), abs(seconds))

    
    
    return time

print(show_time(49, 3600, 61))
print(show_time(-1, -7200, -3700))
print(show_time(23, 59, 60))