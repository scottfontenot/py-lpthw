# "edn=' '" puts a space after the " ? " AND doesn't go to a newline.
print("How old are you?", end=' ')
age = input()
# converts input to an integer before assigning it to age. Throws error if input is a string
#age = int(input())
# pass 'age' to repr() to get the python type of variable (string, or integer)
print(">>> age =", repr(age))
print("How tall are you?", end= ' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} pounds heavy.")



