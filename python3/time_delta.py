#! /bin/python3

import math
import os
import sys
from dateutil import parser
import datetime as dt

def time_delta(t1, t2):
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)
    
    delta = t2 - t1
    seconds = delta.seconds
    return(seconds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = str(time_delta(t1, t2))
        fptr.write(delta + '\n')

    fptr.close()
