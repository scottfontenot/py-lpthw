# argv means argument vector or variable. This holds the arguments you pass to your python script when you run it.
from sys import argv

# read the WYSS section for how to run this 

script, first, second, third = argv

# what is argv? use print to discover, returns a list
print(">>>> argv=", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

