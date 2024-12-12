n=int(input('enter a number'))
try:
    if n > 0:
        print(n**2)
    else:
        raise ValueError('input is -ve')
except Exception as e:
    print(e)
