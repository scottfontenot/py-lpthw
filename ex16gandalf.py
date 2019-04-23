name = "Gandalf"
extendedName = "the Grey"
age = 84
IQ = 149.9
print('type(name):', type(name))  # type(name): <class 'str'>
print('type(age):', type(age))  # type(age): <class 'int'>
print('type(IQ):', type(IQ))  # type(IQ): <class 'float'>

# Gandalf the Grey's age is 84 with incredible IQ of 149.900000
print('%s %s\'s age is %d with incredible IQ of %f ' %
      (name, extendedName, age, IQ))

#Same output can be printed in following ways:


print('{0} {1}\'s age is {2} with incredible IQ of {3} '.format(
    name, extendedName, age, IQ))          # with help of older method
print('{} {}\'s age is {} with incredible IQ of {} '.format(
    name, extendedName, age, IQ))          # with help of older method

# Multiplication of 84 and 149.900000 is 12591.600000
print("Multiplication of %d and %f is %f" % (age, IQ, age*IQ))

#storing formattings in string

sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg': sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print(a)    # "i am a python string!"
print(b)   # "i am a python string!"
print(c)    # "with an arg!"
print(d)   # "with an arg!"
