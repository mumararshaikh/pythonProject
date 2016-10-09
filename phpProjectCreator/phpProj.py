#usr/bin/python

########################################
#   @Version 0.1
#   @author mohammedshaikh
#   @Desc : Create php project directory
#           And start PHP Server
#---------------------------------------

import os, sys,re, thread

def userInput(message, pattern):
    while True:
        userInput = raw_input(message)
        if re.match(pattern, userInput):
            return userInput
        print('Invalid directory name, Enter again')

def phpServer(ipAddr, pathOfServer):
    print  #To start PHP Server
    os.system("cd "+pathOfServer)
    os.system("php -S "+ipAddr)

def startBrowser(browserName, ipAddr):
    print #detect os
    commandForSys = browserName + " http://" + ipAddr
    os.system(commandForSys)  # iceweasel

def createDir(projName):
    syP = projName+'/sys'
    puP = projName+'/Public'
    
    #Create array of path
    pathList = [syP,syP+'/class',syP+'/core',syP+'/conf',puP, puP+'/css',puP+'/js',puP+'/jquery']
    
    #Create main project directory
    os.mkdir(projName, 0755)
    
    #Iterate through list and create Subproject
    for eachPath in pathList:
        os.mkdir(eachPath, 0755)
        
    #Display status
    print "Directory",projName,"Created."
    print "With subdirectory :"
    for eachPath in pathList:
        print eachPath
    print "Task end"
    

displayMessage = "Enter the name of project : "
pattern = '^[A-Za-z_]{2,8}$'

#Ask user to enter a name of project
projName = userInput(displayMessage, pattern)

#Create directory
createDir(projName)

ipAddr = "127.0.0.5:9898"
pathOfServer = projName + '/Public'
browserName = "iceweasel"

#Start new thread for starting server
thread.start_new_thread(phpServer,(ipAddr, pathOfServer))

#start another thread for browser
thread.start_new_thread(startBrowser,(ipAddr, browserName))

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


