start = input("Введите начальное значение диапазона: ")
end = input("Введите конечное значение диапазона: ")

try:
    start = int(start)
    end = int(end)
except ValueError as error:
    print(error)
    exit()

total = 0

current_number = start
while current_number <= end:
    total += current_number
    current_number += 1

print("Сумма всех чисел в заданном диапазоне от", start, "до", end, "равна:", total)
