from xml.dom import INVALID_STATE_ERR


class invalidAgeException(Exception):
    def __init__(self,msg='age is not valid'):
        self.msg=msg

class vote:
    def __init__(self):
        pass
    def check_age(self,age):
        if age >= 18:
            return ('you are eligible')
        else:
            raise invalidAgeException('age is not valid')
obj=vote()
try:
    age=12
    result=obj.check_age(age)
    print(result)
except invalidAgeException as e:
    print(e)

