f=open('07_File_Handling/hello.txt','w')
f.write('\n Python is best for DSA')
f.close()
#to read file content
f=open('07_File_Handling/hello.txt','r')
print(f.read())
f.close()

#create a file
# created_file= open('amyra.csv','x')
# print(open('amyra.csv','r').read()==False)

f=open('amyra.csv','a')
f.write("\nI will gain freedom. I will be stronger.")
f.close()
f=open('amyra.csv','r')
print(f.read())

print("Filename: ", f.name)
print("Mode: ",f.mode)
print("Is closed? ",f.closed)

f.close()
print("Is closed? ",f.closed)

#using with

with open('07_File_Handling/hello.txt', 'r') as file:
    content=file.read()
    print(content)

#reading a file line by line
L=["apple\n","mango\n","banana\n","pineapple\n"]
f=open('07_File_Handling/fruits.txt','w')
f.writelines(L)
f.close()

f=open('07_File_Handling/fruits.txt','r')
cnt=0
print("Using for loop:")

for line in f:
    cnt+=1
    print('Line{}:{}'.format(cnt,line.strip()))
f.close()

#using list comprehension
with open('07_File_Handling/fruits.txt') as f:
    l=[line for line in f]
print(l)

with open('07_File_Handling/fruits.txt') as f:
    l=[line.rstrip() for line in f]
print(l)

#using readlines
f=open('07_File_Handling/fruits.txt')
Lines=f.readlines()
cnt=0
for line in Lines:
    cnt+=1
    print('Line{}:{}'.format(cnt,line.strip()))
f.close()


#using readline()
f=open('07_File_Handling/fruits.txt')
line=f.readline()
while line:
    print(line.strip())
    line=f.readline()
f.close()