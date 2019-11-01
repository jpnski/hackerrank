#! /bin/bash

input="/dev/stdin"

while read -r line;
do
    echo "${line:2:1}"
done < "$input"
