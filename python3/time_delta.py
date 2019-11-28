#! /bin/python3

import datetime as dt
from dateutil import parser

def time_delta(t1, t2):
    t1 = dt.datetime.strptime(t1, "%a %d %B %Y %H:%M:%S %z")
    t2 = dt.datetime.strptime(t2, "%a %d %B %Y %H:%M:%S %z")
    
    delta = str(int(abs(t1 - t2).total_seconds()))
    return(delta)

if __name__ == '__main__':
    n = int(input())
    arr = []
    
    for num in range(n):
        t1 = input()
        t2 = input()
        arr.append((t1, t2))

    deltas = [time_delta(x, y) for x, y in arr]
    for val in deltas:
        print(val)

