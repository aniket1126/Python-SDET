file=open('/file handling/practice session 20/example.txt', 'r')
content=file.read()
words=content.split()
print(len(words))