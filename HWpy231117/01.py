acceleration = input("Введите ускорение (м/с^2): ")
initial_velocity = input("Введите начальную скорость (м/c): ")
time = input("Введите время (секунды): ")

try:
    acceleration = float(acceleration)
    initial_velocity = float(initial_velocity)
    time = float(time)
except ValueError as error:
    print(error)
    exit()
    
distance = initial_velocity * time + 0.5 * acceleration * time ** 2
print("Тело окажется на расстоянии", distance, "метров.")
