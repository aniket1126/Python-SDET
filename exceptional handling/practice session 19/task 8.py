class InsufficientBalanceException(Exception):
    def __init__(self,msg='balance not available'):
        self.msg=msg
        super().__init__(self.msg)

class bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,n):
        if n > 0 and n <= self.balance:
            self.balance -= n
            print(f'withdraw sucessfull: new balance: {self.balance}')
        else:
            raise InsufficientBalanceException('exceeds amount')

balance=2000
account=bankaccount(balance)

try:
    amount_to_withdraw=2503
    account.withdraw(amount_to_withdraw)
except InsufficientBalanceException as e:
    print(e)

