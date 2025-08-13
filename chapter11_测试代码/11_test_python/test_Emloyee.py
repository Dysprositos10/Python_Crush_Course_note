import pytest
from Employee import Employee

@pytest.fixture #定义装饰器
def salary_amount():#这个函数创建并返回一个 Employee 对象。
    salary_amount = Employee('lihua',10000)
    return salary_amount

def test_give_raise(salary_amount):
    assert salary_amount.give_raise() == 15000