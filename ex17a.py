from sys import argv
from os.path import exists

# takes 3 arguments
script, from_file, to_file = argv  # pylint: disable=unbalanced-tuple-unpacking
open(to_file, 'w').write(open(from_file).read())



#print(f"Copying from {from_file} to {to_file}")
