#usr/bin/python

import os, sys

#Ask user to enter a name of project
projName = raw_input("Enter the name of project : ")

path = projName
os.mkdir(path, 0755)

print "Directory",path,"Created."
