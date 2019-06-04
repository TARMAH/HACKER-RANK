from itertools import combinations

n = float(input())
LETTERS = list(input().split())
Combination_Length = int(input())

count = 0

COMBINATIONS = list(combinations(LETTERS,Combination_Length))

for i in COMBINATIONS:
    
    if 'a' in i:
        count = count + 1

print("{0:.4f}".format(round(count/len(COMBINATIONS),4))) 