class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start_engine(self):
        print(f'{self.model} the engine is starting')

obj=car('volvo','cx1',2019)
obj.start_engine()
obj1=car('tata','nexon',2019)
obj1.start_engine()
