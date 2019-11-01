#! /bin/bash

input="./practice7_input.txt"

while read -r line;
do
    echo "${line:1:1}${line:6:1}"
done < "$input"
