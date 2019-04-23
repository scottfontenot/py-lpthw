# call this by using 2 arguments, ex15.py and ex15_sample.txt

from sys import argv
# get the file name from user
script, filename = argv

# may have to write (filename, encoding="utf-8")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

# besides argv, you can also use input with files
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())