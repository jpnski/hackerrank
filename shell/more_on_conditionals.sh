#! /bin/bash
read a
read b
read c

if [[ $a == $b && $b == $c && $a == $c ]]
then
echo "EQUILATERAL"
fi

if [[ $a == $b && $a != $c || $b == $c && $b != $a || $c == $a && $c != $b ]]
then
echo "ISOCELES"
fi

if [[ $a != $b && $b != $c && $a != $c ]]
then
echo "SCALENE"
fi 
