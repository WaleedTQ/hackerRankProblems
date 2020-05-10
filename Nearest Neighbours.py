#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closestStraightCity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY c
#  2. INTEGER_ARRAY x
#  3. INTEGER_ARRAY y
#  4. STRING_ARRAY q
#

def findDistance(x1,y1,x2,y2):
    return abs((x1-x2)+(y1-y2))

def closestStraightCity(c, x, y, q):
    closestCities = []
    for i in range (0, len(c)):
        if(x.count(x[i]) == 1 and y.count(y[i]) == 1):
            closestCities.append("NONE")
            continue
        else:
            nearestCity = ""
            nearestDistance = 9999999999
            for j in range (0, len(c)):
                if not (i == j):
                    if (x[i] == x[j]) or (y[i] == y[j]):
                        dist = findDistance(x[i],y[i],x[j],y[j])
                        if (nearestDistance > dist):
                            nearestDistance = dist
                            nearestCity = c[j]
            closestCities.append(nearestCity)

    return closestCities

    # Write your code here

###Hacker Rank input code here###
