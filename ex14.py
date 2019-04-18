from sys import argv

script, user_name = argv
prompt = '> '
# You know you can make a variable with a string in it, and add two strings together.
# prompt = f'{script} ({user_name})> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

# catch the errors at the input so place the int() here rather than doing {int(age)} in line 21
print(f"How old are you {user_name}? ")
age = int(input(prompt))

#print(f"You're {age}. What kind of computer do you have? ")
print(f"You're {age}. What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
