import os
import string

folder = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(folder,'input.txt')) as f:
    data = f.read()

# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

# Create a structure of each compartment within each bag based on half the "size" (len) of the bag items
all_packs_split = [[x[:int(len(x)/2)],x[int(len(x)/2):]] for x in data.splitlines()]
all_packs = [x for x in data.splitlines()]

# Create a priority map using the ascii_letters list and assign their values
priority_map = {}
for alphaindex in range(len(string.ascii_letters)):
    priority_map[string.ascii_letters[alphaindex]] = alphaindex + 1

# Function to return the priorities
def bag_check(bag):
    both_items = []
    for item in set(bag[0]):
        if item in set(bag[1]):
            both_items.append(item)
    
    item_priorities = [priority_map.get(item) for item in both_items]

    return item_priorities
    # return both_items

def group_check(packs):
    # Cluster packs together in groups of 3
    grouped_packs = [[packs[x+group*3] for x in range(3)] for group in range(len(packs) // 3)]

    badges = []

    for group in grouped_packs:
        for item in set(group[0]):
            if item in set(group[1]) and item in set(group[2]):
                badges.append(priority_map.get(item))
    
    return badges

print(all_packs_split)
print(priority_map)

print(sum([sum(bag_check(pack)) for pack in all_packs_split]))

print(sum(group_check(all_packs)))