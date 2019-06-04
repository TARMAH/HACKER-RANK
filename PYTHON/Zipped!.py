M,N = input().split()

LIST = []
for _ in range(int(N)):
    LIST = LIST + [list(map(float,(input().split())))]

ZIPPED = zip(*LIST)

for part in ZIPPED:
    print(sum(part)/len(part))