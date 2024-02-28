km_to_miles = 0.621371
kilometers = input("Введите количество километров: ")

try:
    kilometers = float(kilometers)
except ValueError as error:
    print(error)
    exit()

miles = kilometers * km_to_miles
print("Это", miles, "миль.")
