try:
    number = int(input("Введите число: "))
except Exception as error:
    print(error)
    exit()
    
divisors = []
for i in range(1, number// + 1):
    if number % i == 0:
        divisors.append(i)
print(f"Делители числа {number} : {divisors}")
