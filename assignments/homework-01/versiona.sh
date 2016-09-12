#!/bin/bash

#first, create the file in the current directory...
touch $(date +"%Y-%m-%d")'_'$1

#then, tell the user it's been done:
echo $(date +"%Y-%m-%d")'_'$1' has been created in the current directory.'
