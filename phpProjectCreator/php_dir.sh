#!/bin/bash

########################################
#   @Version 0.1
#   @author mohammedshaikh
#   @Desc : Create php project directory
#           And start PHP Server
#---------------------------------------

echo "Welcome to PHP project creator."
echo "version : 0.1v"
echo "\n"

if [ $1 = "-f" ];then
	if [ -n $2 ];then
		directory=$2
	else
		echo "Type -f directory_name"
	fi
else
	echo "Type name of project directory"
	read direc
	directory=$direc
fi
echo "Creating project directory...."
if [ -d $directory ]; then
	echo "Directory exist, Choose other name"
else
	mkdir $directory
	cd $directory
	mkdir sys html
	mkdir sys/core sys/class sys/config
	mkdir html/asset html/asset/js html/asset/css html/asset/img html/other
	echo "Project direcory created"\n
	ls -R
	echo "Starting server :"
	php -S 127.0.0.3:8989
fi

