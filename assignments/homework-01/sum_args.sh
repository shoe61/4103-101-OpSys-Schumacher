#!/bin/bash

sum=0

#loop through each argument in $@, the list of all arguments
for arg in $@

do

   ((sum+=arg))

done

echo $sum

