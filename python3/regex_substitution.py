#! /bin/python3

import sys
import re

for i, line in enumerate(sys.stdin):
    if i != 0:
        line = line.strip('\r\n') 
        line = re.sub(r'(?<= )\&{2}(?= )', 'and', re.sub(r'(?<= )\|{2}(?= )', 'or', line))
        print(line)
