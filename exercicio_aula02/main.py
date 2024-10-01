from fastapi import FastAPI

app = FastAPI()

employees = [
    {
        "employee_id": 1,
        "name": "Alice",
        "position": "Software Engineer",
        "salary": 75000
    },
    {
        "employee_id": 2,
        "name": "Bob",
        "position": "Data Analyst",
        "salary": 65000
    },
    {
        "employee_id": 3,
        "name": "Charlie",
        "position": "Product Manager",
        "salary": 90000
    },
    {
        "employee_id": 4,
        "name": "Diana",
        "position": "UX Designer",
        "salary": 70000
    }
]

requests = [
    {
        "request_id": 101,
        "employee_id": 1,
        "status": "approved",
        "duration_days": 5
    },
    {
        "request_id": 102,
        "employee_id": 2,
        "status": "pending",
        "duration_days": 3
    },
    {
        "request_id": 103,
        "employee_id": 3,
        "status": "rejected",
        "duration_days": 7
    },
    {
        "request_id": 104,
        "employee_id": 4,
        "status": "approved",
        "duration_days": 10
    },
    {
        "request_id": 105,
        "employee_id": 1,
        "status": "pending",
        "duration_days": 2
    }
]

@app.get('/employees')
def get_employees():
    return {
        'employees': employees
    }

@app.get('/employees/{id}')
def get_employee(id: int):
    for employee in employees:
        if id == employee['employee_id']:
            return {
                'employee': employee
            }
    return {
        'message': 'Not Found'
    }

@app.get('/vacation/{request_id}')
def get_request_vacation(request_id: int):
    for request in requests:
        if request_id == request['request_id']:
              return {
                'request': request
            }
    return {
        'message': 'Not Found'
    }

@app.get('/vacations', summary='Get requests', description='List all requests')
def get_vacations(status: str = None, min_duration:int = None, max_duration: int = None):
    vacations = requests

    if status: 
        vacations = [vacation for vacation in vacations if status == vacation['status']]

    if max_duration:
        vacations = [vacation for vacation in vacations if vacation['duration_days'] <= max_duration]

    if min_duration:
        vacations = [vacation for vacation in vacations if vacation['duration_days'] >= min_duration]

    return {
        'requests': vacations
    }


    