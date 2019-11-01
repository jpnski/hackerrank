#! /bin/bash

read var

if [[ $var == "Y" || $var == "y" ]]
then
echo "YES"
fi
if [[ $var == "N" || $var == "n" ]]
then
echo "NO"
fi
