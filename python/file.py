import os
filename = raw_input("Enter a file name: ")
try:
 f = open (filename, "r")
 print f.readline()
except IOError:
 print "There is no file named", filename
