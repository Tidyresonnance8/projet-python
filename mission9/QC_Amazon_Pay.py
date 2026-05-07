class EmployeeDidntWorked(Exception):
    pass
class EmployeeWorkedNegatively(Exception):
    pass
class EmployeeWorkedTooMuch(Exception):
    pass
class PayIsNegative(Exception):
    pass
class PayIsTooBig(Exception):
    pass

def pay_employee(Employee,hours_worked):
    if hours_worked == 0:
        raise EmployeeDidntWorked("l'employé a travaillé 0 heure")
    if hours_worked < 0:
        raise EmployeeWorkedNegatively("l'employé a travaillé moins de 0 heure")
    if hours_worked > 744:
        raise EmployeeWorkedTooMuch("l'employé a travaillé plus d'heures que nécessaire")
    if Employee.pay < 0:
        raise PayIsNegative("le salaire de l'employé est négative")
    if Employee.pay > 100:
        raise PayIsTooBig("le salaire de l'heure est plus élevé que 100$")
    salary = hours_worked * Employee.pay
    Employee.receive_salary(salary)