#! /bin/bash

input="/dev/stdin"

while read -r line;
do
    echo "${line:1:6}"
done < "$input"
