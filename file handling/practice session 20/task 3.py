import datetime
file=open('/file handling/practice session 20/example.txt', 'a')
curr=datetime.datetime.now()
file.write(curr)

file.close()
print('done')