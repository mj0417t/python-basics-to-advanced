with open("07_File_Handling/file.txt", "w", encoding="utf-8") as f:
    f.write("Created using write mode.\n")
    f.write("Second line.\n")



with open("07_File_Handling/file.txt", "r", encoding="utf-8") as f:
    print(f.read())


with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Appended line.\n")

with open("file.txt", "r", encoding="utf-8") as f:
    print(f.read())

try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write("Created using exclusive mode.\n")
except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")

#writes a list of lines
lines= ["First line\n", "Second line\n", "Third line\n"]
with open ("07_File_Handling/file1.txt","w",encoding="utf-8") as f:
    f.writelines(lines)

with open("07_File_Handling/file1.txt", "r", encoding="utf-8") as f:
    print(f.read())

#join + single write (often cleaner)
lines = ["Line A", "Line B", "Line C"]
text = "\n".join(lines) + "\n"
with open("07_File_Handling/file2.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("07_File_Handling/file2.txt", "r", encoding="utf-8") as f:
    print(f.read())

#writing to a binary file
data = b'\x00\x01\x02\x03\x04'
with open("07_File_Handling/file.bin", "wb") as f:
    f.write(data)

with open("07_File_Handling/file.txt", "r+", encoding="utf-8") as f:
    content=f.read()
    f.write('\nThis is a new line.')

with open('07_File_Handling/example.txt', 'w+') as file:
    file.write('Hello, world!')
    file.seek(0)
    content = file.read()