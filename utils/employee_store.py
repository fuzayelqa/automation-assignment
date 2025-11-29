import json
from pathlib import Path

EMP_FILE = Path("data/employees.json")

def _load_all():
    if not EMP_FILE.exists():
        return []
    with open(EMP_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def _save_all(employees):
    EMP_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(EMP_FILE, "w", encoding="utf-8") as f:
        json.dump(employees, f, indent=2)

def add_employee(first_name, last_name, employee_id, username, password):
    employees = _load_all()
    emp = {
        "firstName": first_name,
        "lastName": last_name,
        "employeeId": employee_id,
        "username": username,
        "password": password,
        "confirmPassword": password
    }
    employees.append(emp)
    _save_all(employees)
    return emp

def get_last_employee():
    employees = _load_all()
    if not employees:
        raise RuntimeError("No employees stored in employees.json")
    return employees[-1]
