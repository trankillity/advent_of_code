import os
import re

folder = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(folder,'input.txt')) as f:
    data = f.read()

data="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

layout,commands = data[0:data.find('\n\n')].splitlines(),data[data.find('move'):]

# Define the layout using list slicing then comprehension. Finally pivot the data so each list is a column then clear out any blanks and remove the column numbers.
laylist = [x[1::4] for x in layout]
laylist = [[col for col in row] for row in laylist]
laylist = [[row[i] for row in laylist] for i in range(len(laylist[0]))]
laylist = [[x for x in y if x != ' '] for y in laylist]
laylist = [x[:-1] for x in laylist]

# Define the commands using a regex expression to split them into groups then convert them to ints.
command_search = r"move (\d+) from (\d+) to (\d+)"
commands = [list(re.search(command_search,x).groups()) for x in commands.splitlines()]
commands = [[int(x) for x in y] for y in commands]

print(laylist,commands)

def move_crates(amount,source,destination):
    print(f"Moving {amount} crates from {source} to {destination}.")
    for move in range(amount):
        cur_crate = laylist[source-1][0]
        laylist[source-1].pop(0)
        laylist[destination-1].insert(0,cur_crate)
        print(f"- Step {move}: {cur_crate}")
    print("Done moving. Current layout:")
    print(laylist)

def move_crates_multi(amount,source,destination):
    print(f"Moving {amount} crates from {source} to {destination}.")
    # Create temporary list of all the grabbed crates
    cur_crates = laylist[source-1][0:amount]
    # Remove the crates from the source using list slicing, ensuring a fallback of an empty list
    laylist[source-1] = laylist[source-1][amount:] if len(laylist[source-1]) > amount else []
    # Add the temporary grabbed crates list to the start of the destination list
    laylist[destination-1] = cur_crates + laylist[destination-1]
    print("Done moving. Current layout:")
    print(laylist)

for command in commands:
    move_crates(command[0],command[1],command[2])
    # move_crates_multi(command[0],command[1],command[2])

# print([x[0] for x in laylist])
