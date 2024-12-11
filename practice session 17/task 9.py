class bankaccount:
    __accountnumber=2001
    __balance=500
    def deposit(self,value):
        self.__balance += value
        print(f"present balance {self.__balance}")
    def withdraw(self,value2):
        if value2 > 0 and value2 <= self.__balance:
            self.__balance -= value2
        else:
            return 'insufficient balance'
        print(self.__balance)


obj=bankaccount()
obj.deposit(20)
obj.withdraw(550)