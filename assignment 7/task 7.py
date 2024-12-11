class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def delete(self):
       print(self.name,self.model)

obj=car('volvo','cx1')
obj.delete()
del obj.name
obj.delete()