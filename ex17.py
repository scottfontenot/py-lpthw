from sys import argv
from os.path import exists

# takes 3 arguments
script, from_file, to_file = argv# pylint: disable=unbalanced-tuple-unpacking
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
# to debug, repr gives you the raw representation, will get a strange output, telling you useful information. Sometimes errors will look like this 
print(">>>> in_file=", repr(in_file))
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abortt.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()
