from djangoninja.model import Employee


def list_employees():
    try:
        return Employee.objects.all()
    except Exception as exc:
        raise exc


def create_employee(data):
    try:
        return Employee.objects.create(**data.dict())
    except Exception as exc:
        raise exc


def retrieve_employee(employee_id):
    try:
        return Employee.objects.get(id=employee_id)
    except Exception as exc:
        raise exc
