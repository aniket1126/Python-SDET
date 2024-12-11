class company:
    company_name="DEL"
    def __init__(self,empname,desig):
        self.empname=empname
        self.desig=desig
    def deisplay(self):
        print(f'{self.empname} , {self.desig} {company.company_name}')
        
obj=company('aniket','SDET')
obj.deisplay()


