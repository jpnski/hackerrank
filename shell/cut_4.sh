#! /bin/bash

input="/dev/stdin"

while read -r line;
do
    echo "${line:0:4}"
done < "$input"
