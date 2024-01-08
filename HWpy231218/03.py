def show_time(hours, minutes=0, seconds=0):
    if seconds // 60 != 0:
        minutes += seconds // 60
        seconds = seconds % 60

    if minutes // 60 != 0:
        hours += minutes // 60
        minutes = minutes % 60

    hours = hours % 24

    text = "%02d:%02d:%02d"
    time = text % (abs(hours), abs(minutes), abs(seconds))

    return time

print(show_time(49, 3600, 61))
print(show_time(-1, -7200, -3700))
print(show_time(23, 59, 60))