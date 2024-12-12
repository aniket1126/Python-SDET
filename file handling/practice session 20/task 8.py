file1=open(r'D:\BEBO\Python-SDET\file handling\practice session 20/example.txt','r')
file2=open(r'D:\BEBO\Python-SDET\file handling\practice session 20/file2','r')
content=file1.read()
content2=file2.read()
file3=open(r'D:\BEBO\Python-SDET\file handling\practice session 20/merge.txt','w')
merge=content+content2
file3.write(merge)
file1.close()
file2.close()
file3.close()





