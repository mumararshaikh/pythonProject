#usr/bin/python

import os, sys,re 

def userInput(message, pattern):
    while True:
        userInput = raw_input(message)
        if re.match(pattern, userInput):
            return userInput
        print('Invalid directory name, Enter again')
        
#Ask user to enter a name of project
displayMessage = "Enter the name of project : "
pattern = '^[A-Za-z_]{2,8}$'

projName = userInput(displayMessage, pattern)

syP = projName+'/sys'
puP = projName+'/Public'

f_List = [syP,syP+'/class',syP+'/core',syP+'/conf',puP, puP+'/css',puP+'/js',puP+'/jquery']

os.mkdir(projName, 0755)

for pathL in f_List:
    os.mkdir(pathL, 0755)

print "Directory",projName,"Created."
print "With subdirectory :"
for Item in f_List:
    print Item

#Start the PHP Server
os.system("cd "+puP)
os.system("php -S 127.0.0.5:9898")

#Starting browser
os.system("iceweasel http://127.0.0.5/9898")

#Create Sub directory
# Main directory
# sys
#  --class
#   ---dbConf.php
#  --core
#   ---init.php
#  --config
#   ---config.php
# public
#  --css
#   ---main.css
#  --js
#   ---main.js
#  --jquery
#  --index.php
#
#---------------------


