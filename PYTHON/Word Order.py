N = int(input())
DICT = dict()

for _ in range(N):
    key = input()
    
    if key not in DICT:
        DICT[key] = 1
    else:
        DICT[key] = DICT[key] + 1

STRING = ""
for key, val in DICT.items():
    STRING=STRING+str(val)+" "

print(len(DICT))
print(STRING)