def calculate(num1: float, num2: float, operator: str) -> float:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        else:
            return num1 / num2
    else:
        return "Ошибка: некорректный оператор"


while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except Exception as error:
        print(error)
        exit()

    operator = input("Введите оператор (+, -, *, /): ")
    result = calculate(num1, num2, operator)
    print(f"Результат: {result}")
    continue_calculation = input("Хотите решить еще один пример? (да/нет): ")
    
    if continue_calculation.lower() != 'да':
        break
