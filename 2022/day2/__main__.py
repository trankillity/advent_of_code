import os
folder = os.path.dirname(os.path.realpath(__file__))

# [Rock, Paper, Scissors]
opponent_map = {"A":1,"B":2,"C":3}
# [Lose, Draw, Win]
player_map = {"X":1,"Y":2,"Z":3}
overall_map = opponent_map | player_map

with open(os.path.join(folder,'input.txt')) as f:
    data = f.read()

# data = """A Y
# B X
# C Z"""

all_rounds = [x.split(" ") for x in data.splitlines()]
# Convert to numerical map
all_rounds = [[overall_map.get(x[0]),overall_map.get(x[1])] for x in all_rounds]

def check_round(opponent,player):
    if (player == opponent):
        return [player, 3]
    elif (player == 1 and opponent == 3) or (player == 2 and opponent == 1) or (player == 3 and opponent == 2):
        return [player, 6]
    else:
        return [player, 0]

def check_round2(opponent,round_result):
    if (round_result == 2):
        # Result in draw
        return [opponent,3]
    elif (round_result == 3):
        # Result in win
        return [1 if opponent == 3 else 2 if opponent == 1 else 3,6]
    elif (round_result == 1):
        # Result in loss
        return [3 if opponent == 1 else 1 if opponent == 2 else 2,0]

total_score = 0

# for round in all_rounds:
#     result = check_round(round[0],round[1])
#     print(result)
#     total_score += sum(result)
#     print(total_score)

for round in all_rounds:
    result = check_round2(round[0],round[1])
    print(result)
    total_score += sum(result)
    print(total_score)
