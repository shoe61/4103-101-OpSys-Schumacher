#!/bin/bash
now=$(date +%Y-%m-%d)
fullname=$1

#filename without extension:
namo=${fullname%.*}

#extension without filename:
extn=${fullname##*$namo}

#string them together and create the new file:
touch $namo'_'$now$extn

#and tell the world:
echo $namo'_'$now$extn
