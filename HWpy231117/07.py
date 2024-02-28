total_sales = input("Введите общую сумму продаж за месяц: ")

try:
    total_sales = float(total_sales)
except ValueError as error:
    print(error)
    exit()

base_salary = 250 
commission = 0.1 * total_sales 
salary = base_salary + commission
print("Зарплата работника составляет $", salary)
