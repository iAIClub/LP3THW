#17
from sys import argv
from os.path import exists#filename as input

script,from_file,to_file= argv

print "Copying from %s to %s" %(from_file,to_file)

# we could do these two on one line too,how?
input= open(from_file)
indata=input.read()

print"The input file is %d bytes llong"% len(indata)

print "Does the output file exist?%r"% exists(to_file)
print"Ready,hit RETURN to cotinue,CTRL-C to abort."
raw_input()

output= open(to_file,'w')
output.write(indata)

print"Alright,all done"

output.close()
input.close()


'''
# The Result .....Any Chinese Character Can not be in the it ,or it will report a wrong!

itifadeMacBook-Pro:~ yyy$ python Documents/Python_LP2THW/ex17.py Documents/Python_LP2THW/test.txt Documents/Python_LP2THW/copied.txt
Copying from Documents/Python_LP2THW/test.txt to Documents/Python_LP2THW/copied.txt
The input file is 61 bytes llong
Does the output file exist?True
Ready,hit RETURN to cotinue,CTRL-C to abort.

Alright,all done
itifadeMacBook-Pro:~ yyy$ 
--- cat 
itifadeMacBook-Pro:~ yyy$ cat Documents/Python_LP2THW/copied.txt
How old are you?
How much do you earn?
Do you have children?
itifadeMacBook-Pro:~ yyy$ 
'''
