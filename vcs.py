import operator
import re
import sys

if len(sys.argv) < 2:
    print("No input file.")
    sys.exit()

pattern = "^([0-9/])*,([0-9:])*,([^+]*),(\+[^,]*),(.*)$"
participants = {}

with open(sys.argv[1], "r", encoding="utf-8-sig") as lines:
    for line in lines:
        matches = re.findall(pattern, line)
        if len(matches) > 0:
            participants[matches[0][2]] = participants.get(matches[0][2], 0) + 1

participants = sorted(participants.items(), key=operator.itemgetter(1), reverse=True)

for participant in participants:
    print(participant[0], "-", participant[1])