from sys import argv

script, filename = argv# pylint: disable=unbalanced-tuple-unpacking

# CTRL-C will not do anything
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# to write a file, open it with mode "w" as a second parameter, if the file exists, opening it in write mode clears out the old data and starts fresh. If the file doesn't exist, a new one is created.
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for threee lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goint to write these to the file.")
# must manage the ends of lines as u write to the file by explicityly inserting the newline character when u want to end a line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
#when done, u have to close the file to make sure that the data is physically written to the disk. When writing, leave nothing to chance.
target.close()

