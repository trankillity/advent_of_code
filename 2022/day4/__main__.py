import os

folder = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(folder,'input.txt')) as f:
    data = f.read()

# data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

data_grouped = []

for line in data.splitlines():
    grp = []
    for col in line.split(','):
        start,end = col.split('-')
        grp.append(list(range(int(start),int(end)+1)))
    data_grouped.append(grp)

def full_overlap_check(group):
    return all(item in group[0] for item in group[1]) or all(item in group[1] for item in group[0])

def any_overlap_check(group):
    return any(item in group[0] for item in group[1]) or any(item in group[1] for item in group[0])

print("Full Overlap: ",sum([full_overlap_check(x) for x in data_grouped]))
print("Any Overlap: ",sum([any_overlap_check(x) for x in data_grouped]))