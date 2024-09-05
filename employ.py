class Employee:
    def __init__(self,id,first_name,last_name,salary):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    def get_full_name(self):
        self.first_name + self.last_name
        print(self.first_name,self.last_name)
    def raise_salary(self,raise_salarys):
        self.raise_salarys=raise_salarys
        self.salary= self.salary + self.raise_salarys
        print(self.salary)
    def get_annual_salary(self):
        return self.salary*12
employee=Employee(744423129,'Nguyen','Duong',1000)
print (employee.get_full_name())
employee.raise_salary(500)
print (employee.get_annual_salary())