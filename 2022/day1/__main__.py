import os
import re as r
# import pandas as pd

folder = os.path.dirname(os.path.realpath(__file__))

groups = []

with open(os.path.join(folder,'input.txt')) as f:
    curgroup = []
    for line in f:
        if r.match('\d',line):
            curgroup.append(int(line))
        else:
            groups.append(curgroup)
            curgroup = []

print(groups)
summedgroup = sorted([sum(x) for x in groups],reverse=True)
print(summedgroup)
print(max(summedgroup))
print(sum(summedgroup[0:3]))

# data = pd.read_csv(os.path.join(folder,'input.txt'))
# print(data)