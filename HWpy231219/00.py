from datetime import date

def newEmployee(fullName: str, birthDate: str, position: str, salary: int) -> dict:
    try:
        firstName, lastName = fullName.split()
        id = len(database)
        employee = {
                    "id": id,
                    "firstName": firstName,
                    "lastName": lastName,
                    "birthDate": birthDate,
                    "hiredDate": date.today(),
                    "firedDate": None,
                    "position": position,
                    "salary": salary
                }
        database.append(employee)
        return {"id": id, "errorDescription": None}
    except Exception as errorDescription:
        return {"id": -1, "errorDescription": str(errorDescription)}


def fireEmployee(id: int) -> dict:
    try:
        database[id].update({"firedDate": date.today()})        
        return {"id": id, "errorDescription": None}
    except Exception as errorDescription:
        return {"id": -1, "errorDescription": str(errorDescription)}


def getEmployeeId(name: str) -> int|set:
    id_set = set() 
    for employee in database:
        for key, value in employee.items():
            if value == name:
                id_set.add(employee["id"])
    if id_set:
        return id_set
    return -1


def getEmployeeRecord(id: int) -> dict:
    return database[id]


def showFiredEmployees() -> list:
    firedEmployees = []
    for employee in database:
        if employee["firedDate"] is not None:
            firedEmployees += [employee]
            break
    return firedEmployees


def getSalaryStats() -> dict:
    salaries = []
    for employee in database:
        if employee["firedDate"] is None:
            salaries += [employee["salary"]]
    salaries = sorted(salaries)
    average_salary = sum(salaries)/len(salaries)
    if len(salaries) % 2 == 0:
        median_salary = (salaries[int(len(salaries)/2)] + salaries[int(len(salaries)/2)-1]) / 2
    else:
        median_salary = salaries[int(len(salaries)/2)]
    stats = {"Общий размер зарплатного фонда компании": sum(salaries), "Максимальная зарплата": max(salaries), "Минимальная зарплата": min(salaries), "Средняя зарплата": average_salary, "Медианная зарплата": median_salary}
    return stats


database = []

print(newEmployee("Агарков Сергей", "2001-03-01", "Программист", 350000))
print(newEmployee("Есимбек Ғалымжан", "2000-02-01", "Программист", 400000))
print(newEmployee("Шагимарданов Тимур", "1996-01-01", "Программист", 300000))
print(newEmployee("Нежельский Александр", "1988-01-01", "Программист", 500000))
print(newEmployee("БектасоваСания", "1990-01-01", "Программист", 500000))
print(fireEmployee(0))
print(fireEmployee(4))
print(getEmployeeId("Ғалымжан"))
print(getEmployeeId("Нежельский"))
print(getEmployeeId("Тимур"))
print(getEmployeeId("Мадина"))
print(getEmployeeRecord(2))
print(showFiredEmployees())
print(getSalaryStats())