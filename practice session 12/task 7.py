class employee:
    name,salary = "aniket",200000
    def update_salary(self,new):
        self.salary += new
    def newsalary(self):
        print(self.salary)

mc=employee()

mc.update_salary(300)
mc.newsalary()

