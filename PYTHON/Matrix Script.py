import re

R,M = map(int,input().split())

LIST = [input() for i in range(R)]


STRING = ''

for j in range(M):
    for i in range(R):
        STRING += LIST[i][j]


#REPLACING THE STRING WITH SPECIFIC PATTERN

print(re.sub(r"([a-zA-Z])[\s!@#$%&]+([a-zA-Z])", r"\1 \2", STRING))
