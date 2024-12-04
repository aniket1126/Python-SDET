class employee:
    def __init__(self,eid,esalary,ename):
        self.eid=eid
        self.esalary=esalary
        self.ename=ename

    def __str__(self):
        return f"EID = {self.eid}\nname = {self.ename}\nsalary {self.esalary}"

obj1=employee('aniket','ASE',60000)
print(obj1)




