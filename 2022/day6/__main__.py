import os
import re

folder = os.path.dirname(os.path.realpath(__file__))

data="""bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

with open(os.path.join(folder,'input.txt')) as f:
    data = f.read()

data = data.splitlines()

def unique_pos(row):
    start_packet_marker = None
    start_message_marker = None
    for i in range(len(row)):
        start_packet_check = [row[i+x] for x in range(4)]
        if len(start_packet_check) == len(set(start_packet_check)) and start_packet_marker is None: start_packet_marker = i+4
        start_message_check = [row[i+x] for x in range(14)]
        if len(start_message_check) == len(set(start_message_check)) and start_message_marker is None: start_message_marker = i+14
        if start_packet_marker is not None and start_message_marker is not None: break
    return [start_packet_marker,start_message_marker]

print([unique_pos(x) for x in data])