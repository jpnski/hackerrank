#! /bin/python3

import math

def theta(a,b):
    hyp = ((a**2 + b**2)**0.5)/2
    adj = b/2 
    theta = int(round(math.degrees(math.acos((adj/hyp)))))
    print(str(theta) + u"\u00b0")

if __name__ == '__main__':
    a = int(input()) 
    b = int(input())

    theta(a,b)
