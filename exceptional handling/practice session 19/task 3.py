mylist=list(map(int,input('enter a list').split()))
idx=int(input('enter a ind'))
try:
    print(mylist[idx])
except Exception as e:
    print(e)