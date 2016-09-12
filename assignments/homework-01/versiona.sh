#!/bin/bash
now=$(date +"%Y-%m-%d")
echo $now
fname=$1
echo $fname
blurp=_
newname=$now$blurp$fname
echo $newname
