# assign 10 to types_of_people
types_of_people = 10
#print(type(types_of_people))

# assign the f-string to x(insert string variable)
x = f"There are {types_of_people} types of people."
# print(type(x))

# assign 2 more variables to a string value
binary = "binary"
do_not = "don't"

# this is a string variable with 2 embedded string variables
y = f"Those who know {binary} and those who {do_not}."
print(">>>> after assign y", y)

print(x)
print(">>>>before printing y", y)
print(y)

# 2 more string variables
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation =  "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# concatenating 2 string variables
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)