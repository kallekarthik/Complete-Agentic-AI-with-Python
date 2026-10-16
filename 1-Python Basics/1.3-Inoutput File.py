myfile=open("myfile.txt","w") # this will create a new file called myfile.txt in the current directory and open it in write mode, if the file already exists, it will overwrite the existing file
myfile.write("Hello World, this is the first line of the file.\n this is the second line") # this will write the string to the file, \n is used to create a new line
myfile.close()
myfile=open('myfile.txt','r')
#cont=myfile.read()
with open('myfile.txt','a') as myfile1:
    contents=myfile1.write('\nThis is the new content of the file, used append mode to add this content to the existing file.')
print(myfile.readlines())
myfile.seek(0) # this will move the cursor to the beginning of the file, so that we can read the contents of the file from the beginning
print(myfile.read())
#print(cont)
myfile.close()


with open('newfile.txt','w') as f:
    f.write('This is a new file created using the with statement, which automatically closes the file after the block of code is executed.')

with open('newfile.txt','r') as f:
    print(f.read()) # this will give an error because the file is closed after the with block is executed
