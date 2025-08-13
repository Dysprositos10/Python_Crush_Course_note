class Employee:
    def __init__(self,name,salary):
        """初始化数据"""
        self.name = name
        self.salary = salary
    def give_raise(self,add_salary=5000):
        '年薪增加5000'
        self.salary +=add_salary
        return  self.salary