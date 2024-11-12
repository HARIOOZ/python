class employe:
    def __init__(self, base_salary):
      self.base_salary=base_salary
    def get_salary(self):
      return self.base_salary()
class manager(employe):
    def __init__(self, base_salary, bonus ):
               super().__init__(base_salary)
               self.bonus=bonus

    def get_salary(self):

          return self.base_salary+self.bonus

class engineer (employe):

     def init (self, base_salary, bonus): 
        super().__init__(base_salary)
        self.bonus=bonus

     def get_salary(self):


        return self.base_salary+self.bonus

manager1=manager(20000,5000)
engineer1=engineer(30000,8000) 
manager2=manager(20000,6000)
employees=[manager1, engineer1, manager2]
for i in employees:
    print(f" emplyee salary: {i.get_salary()}")