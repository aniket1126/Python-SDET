#key benefits of functions
#code reuseablility
#imporve readability
#easier debugging

#declare the function
#def myfun():
#    print("hello")
#myfun()                      #calling the function

#declaring the function
#def myfun(name):               #declaring the function name=david
#    print("hello",name)
#myfun("david")

#not printing but returning some values
#def cal(a,b):
 #   return(a+b)

#print(cal(10,20))
#sum = cal(10,30)
#print(sum)

#return none                   when nothing is return it will print none
#def fun():
#    return
#print(fun())

#def fun(i):
#    i=10
#print(fun(10))


#example 5
#def cal(a,b):
#    print(a+b)
#print(cal(10,20))

#def cal(a,b):
#    return (a+b)
#print(cal(10,20))

#types of function
#function that does not argument not return any value #none
#function that does not argument but return some value
#function that takes argument not return any value     #print
#function that take argument also return some value

#add 2 number using function
#def add(a,b):
#    print(a+b)

#print(add(10,20))


#fact of a number
#def fact(n):
#    f = 1
#    while n > 0:
#        f = f * n
#       n -= 1
#    print(f)
#fact(5)

#global variable.local variable
#global_variable=20
#def fun():
#    local_variable=10
#    print(local_variable)

#print(global_variable)
#fun()

#when global and local val has same name
#xy=100
#def cal():
#    xy=200
#    print(xy)

#cal()
#print(xy)

#chnage the value of global variable inside the function
#xy=100
#def cal():
#    global xy
#    xy=200
#   print(xy)

#print(xy)
#x=100
#def cal():
#    global x
#    x=500
#    print(x)

#cal()
#print(x)


#arguments
#positional argument                         fun(i,j) assign value on the basis of index
#keyword argument                          assign value inside the argument(a=1,b=2)
#default argument
#variable length argument
#eyword only variable length argument


#def fun(a=10,b=20):
#    print(a,b)
#fun()

#default


#
#def greet(name,greetmsg):
#    print(greetmsg+ " " + name)

#greet("aniket","hiii")
#greet(name="aniket", greetmsg="hiii")

#combination of arguments
#def fun(a,b,c):
#    print(a,b,c)

#fun(10,20,30)                  postitonal argument
#fun(a=10,b=20,c=30)            keyword argument
#fun(10,b=20,30)              it is error bcz no positonal argument will come after keyword argumnet

#def large(a,b):
#    if a>b:
#        print(a)
#    else:
#        print(b)
#print(large(10,20))

#def area(l,b,h=10):
#    ar=l*b*h
#    print(ar)
#area(10,20)

#def address(name,dept,add="chd"):
#    print(name,add,dept)
#address("aniket","it")

#def discount(p,r,t):
#    final = p*r*t/100
#    print(final)

#discount(1000,2,5)

#lamda function
#function which has no name
#x=lambda a:a+10                     (a+10 is expression it is only 1 argument is more)
#print(x(5))

#x=lambda a,b:a*b
#print(x(5,5))
#x=lambda a,b,c:a*b*c
#print(x(5,5,5))

#list1=(1,2,3,4,5,6,7,8,9)
#def even(a):
#    if a%2==0:
###  else:
#      print()
#even(2)

#evenno=list(filter(lambda x:x%2==0,list1))
#print(evenno)


#city=['jaipur','kota','chd','delhi','muzza']
#def length(city):
#    return len(city)

#sort=sorted(city,key=length,reverse=True)
#print(sort)
#sortno=sorted(city,key=lambda x:len(x),reverse=True)
#print(sortno)


#no = [1,2,3,4]
#sq=list(map(lambda x:x**2,no))
#print(sq)

#reduce function                                   (less readable,complex problem lambda porblems)
#z=reduce(lambda x,y:x+y,[1,2,3,4])                (gives a single digit ans is 10)
#print(z)

#zip tuple()
#subject=["math","english","hindi"]
#marks=[40,50,60]
#a=zip(subject,marks)
#res=list(a)
#print(res)

#variable argument
#*args ------ positional variable length argument
#**kwargs---- keyword variable length argument
#allow a function to accept any  no of positional argument
#which allow to be passed as a tuple

#example 1
#def greet(*name):
#    print("hello",{name})

#print("david")
#greet("daivd","aniket","john","marry")          (postitonal variable length argument)

#exapmle 2
#def info(**kwargs):
#    for key,value in kwargs.items():
#        print(f'{key}:{value}')                   use of dictionary
#info(name="aniket",id=20)


#def dis(*args,**kwargs):
#    print("positional ",args)
#    print("keyword",kwargs)
#dis(1,2,3,"aniket",age=30,id=102,city="chd")


#def greet(name,*args):
#    print(name,args)
#greet("aniket","david","bob",30)


#def greet(name,*args,**kwargs):
#    print(name)
#    for i in args:
#        print(i)
#    for i,j in kwargs.items():
#        print(f'{i},{j}')

#greet(300,'aniket','marry',25,name1='john',age=20)

#def fun(n):
#    if n==0 or n==1:               (factorial of a number using recursion)
#        return 1
#    else:
#        return n*fun(n-1)
#print(fun(5))













