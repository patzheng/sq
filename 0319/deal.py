import pandas as pd

file = open("rrr2.csv")
result = {}
while 1:
    line = file.readline().rstrip()
    if not line:
        break
    result[line.split(',')[0]] = line.split(',')[1]
file = open("old")
while 1:
    line = file.readline().rstrip()
    if not line:
        break
    #print(line)
    xx = result[line]
    print(xx)
