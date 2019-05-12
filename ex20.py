# import argv variables from the sys module
from sys import argv

# assign the first and second arguments to the two variables. This sets up 'argv' to accept the script and 'test.txt' file as input
script, input_file = argv
# Remember to call this script use: ex20.py test.txt

# define a function 'print_all' which reads and prints the contents of a file, with one file object, the variable "f", as parameter
def print_all(f):
    print(f.read())

# define a function 'rewind' to set the input files current position to 0 using the seek()
def rewind(f):
    f.seek(0)

# define a function 'print_a_line' to accept an integer(current_line), denoting the line to read and then reads the line with 'readline()'. Note readline() leaves a \n character at the end of the line, so this automatically advances the file position by 2 line for everytime the function is called.
def print_a_line(line_count, f):
    #test if two variables are carrying the same value
    print("line_count equal to current_line?:", (line_count==current_line))
    #print the number and contents of a line
    print(line_count, f.readline())

# sets 'current_file' equal to the file object, which is defined in the arguments(or is it parameters?) when running the script, our test.txt file. 
current_file = open(input_file)

# prints the whole file on a new line under this string 
print("First let's print the whole file:\n")

# call the print_all function using current_file as the parameter to print the whole file "f"
print_all(current_file)

# print string
print("Now let's rewind, kind of like a tape.")

# call the rewind function to go back to the beginning of th file. Calls rewind() with the parameter 'current_file' which should reset the files current position to 0. IF you comment out this line, running the script doesn't print the lines out. THis suggests that the files current position at this point is at the end of the file.
rewind(current_file)

#print string
print("Let's print three lines:")

# set variable current line to 1
current_line = 1
# call print_a_line function to print current line
print_a_line(current_line, current_file)

# increment current line by 1, sets current_line to line 2
current_line += 1
# call print_a_line function to print current line
print_a_line(current_file, current_file)

# increment line by 1, setting current line to line 3
current_line += 1
# call print_a_line function and print current line 
print_a_line(current_line, current_file)