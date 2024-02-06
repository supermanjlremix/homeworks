import mymodule

if __name__ == "__main__":
    print(mymodule.newEmployee(
        "Агарков Сергей", "2001-03-01", "Программист", 350000))
    print(mymodule.newEmployee(
        "Есимбек Ғалымжан", "2000-02-01", "Программист", 400000))
    print(mymodule.newEmployee(
        "Шагимарданов Тимур", "1996-01-01", "Программист", 300000))
    print(mymodule.newEmployee(
        "Нежельский Александр", "1988-01-01", "Программист", 500000))
    print(mymodule.newEmployee(
        "БектасоваСания", "1990-01-01", "Программист", 500000))
    print(mymodule.fireEmployee(0))
    print(mymodule.fireEmployee(4))
    print(mymodule.getEmployeeId("Ғалымжан"))
    print(mymodule.getEmployeeId("Нежельский"))
    print(mymodule.getEmployeeId("Тимур"))
    print(mymodule.getEmployeeId("Мадина"))
    print(mymodule.getEmployeeRecord(2))
    print(mymodule.showFiredEmployees())
    print(mymodule.getSalaryStats())
