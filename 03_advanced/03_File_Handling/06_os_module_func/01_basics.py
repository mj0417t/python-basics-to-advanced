import os
cwd=os.getcwd()
print('Curr working dir: ',cwd)

def curr_path(label):
    print(f"Current working dir: {label}")
    print(os.getcwd())
    print()
curr_path("before")
os.chdir('../')
curr_path('after')
os.chdir('C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics')
print('Curr working dir: ',cwd)

# #creating a directory
# directory="07_File_Handling/sample"
# parent_dir='C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/'
# path=os.path.join(parent_dir,directory)

# os.mkdir(path)

# print("Directory '% s' created" % directory)

# directory = "Geeks"
# parent_dir = "C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling"
# mode = 0o666
# path = os.path.join(parent_dir, directory)
# os.mkdir(path, mode)
# print("Directory '% s' created" % directory)

# #using mkdirs
# directory="mj"
# parent_dir="C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/Geeks/authors"
# path=os.path.join(parent_dir,directory)
# os.makedirs(path)
# print("Directory '% s' created" % directory)

#listing out files and directories
path='/'
dir_list=os.listdir(path)
print("Files and directories in '", path,"':")
print(dir_list)

# file='file1.txt'
# loc='C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/'
# path=os.path.join(loc,file)
# os.remove(path)

# directory='sample'
# parent='C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/'
# path=os.path.join(parent,directory)
# os.rmdir(path)

#set read write permission for own
os.chmod('C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/file.txt',0o600)

stats=os.stat('C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/file.txt')
print("Size: ", stats.st_size,"bytes")
print("Last Modified: ",stats.st_mtime)
print("Permissions: ", oct(stats.st_mode)[-3:])

print(os.name)

try:
    filename = 'GFG.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
  print('Problem reading: ' + filename) # type: ignore


result = os.path.exists("C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/file.txt")
print(result)

size = os.path.getsize("C:/Users/musar/source/repos/mj0417t/python-basics-to-advanced/basics/07_File_Handling/file.txt")
print("Size of the file is", size," bytes.")