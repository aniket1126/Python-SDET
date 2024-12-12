name=input('enter name of file')
file=open(f"D:/BEBO/Python-SDET/file handling/practice session 20/{name}","r")
lines=file.readline()
num_lines=len(lines)
num_words=sum(len(line.split()) for line in lines)
num_characters=sum(len(line) for line in lines)

print(f'number of lines: {num_lines}')
print(f'number of words: {num_words}')
print(f'number of characters: {num_characters}')



