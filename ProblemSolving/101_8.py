# 101 Challenge -> Binary Challenge

#!/bin/python

import sys


n = int(raw_input().strip())

binaryn = bin(n)[2:]
#print binaryn
result = {"0":0, "1":0}
max = 0
#binaryn = str(n)
for char in binaryn:
    if char == "1":
        result["1"] += 1
    if result["1"] > max:
        max = result["1"]
    if char == "0":
        result["0"] += 1
        result["1"] = 0
print max
