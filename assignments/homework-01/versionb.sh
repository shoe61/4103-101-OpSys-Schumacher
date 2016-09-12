#!/bin/bash
now=$(date +%Y-%m-%d)
fullname=$1

#filename without extension:
namo=${fullname%.*}

#extension without filename:
extn=${fullname##*$namo}

#string them together:
echo $namo'_'$now$extn
