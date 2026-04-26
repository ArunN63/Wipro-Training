class employee:
    def __init__(self, emp_id,name,salary):
        self.__emp_id=emp_id
        self.__name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def get_emp_id(self):
        return self.__emp_id
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def set__salary(self,salary):
        self.__salary=salary
    def display(self):
        print("ID:",self.__emp_id)
        print("Name:",self.__name)
        print("salary:",self.__salary)
    def hike(self, percent):
        increase=self.__salary+percent/100
        self.__salary+=increase
        print("salary increased by:",percent,"%")
emp1=employee(1,"mohan",20000)
emp1.display()
emp1.hike(10)
emp1.display()



