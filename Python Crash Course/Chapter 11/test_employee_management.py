import pytest
from employee_management import Employee

@pytest.fixture
def create_employee():
    test_employee = Employee('John','Smith',50000)
    return test_employee

def test_give_default_raise(create_employee):
    create_employee.give_raise()
    assert create_employee.salary == 55000

def test_give_default_raise(create_employee):
    create_employee.give_raise(10000)
    assert create_employee.salary == 60000