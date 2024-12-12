#FILE HANDLING WITH TEXT FILE
'WRITING THE DATA INTO TEXT FILE'
import os

#open()
# file=open('D:/BEBO/Python-SDET/arrays/aniket.txt',"w")
# file.write('first instruction\n')
# file.write('2nd instruction\n')
# file.write('3rd instruction\n')
# file.write('4th instruction\n')
# file.close()
# print('completed')

'READING DATA FROM TEXT FILE'
file=open("D:/BEBO/Python-SDET/arrays/aniket.txt","r")
print(file.read())
print(file.readline())
print(file.readable())
file.close()

'APPENDING DATA INTO TEXT FILE'
# file=open("D:/BEBO/Python-SDET/arrays/aniket.txt","a")
# print(file.write('this is 6th inst\n'))
# print(file.write('this is 7th inst\n'))
# file.close()

'REMOVING THE FILE'
import os
try:
    os.remove('D:/BEBO/Python-SDET/arrays/aniket.txt')
    print('the file is deleted')
except FileNotFoundError as e:
    print(e)

'REMOVING THE DIRECTORY'
# os.rmdir('D:/BEBO/Python-SDET/arrays/aniket.txt')
# print('the dir is deleted')
