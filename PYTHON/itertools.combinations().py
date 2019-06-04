from itertools import combinations

STRING,n= input().split()

for numberOfCombinations in range(1,int(n)+1):
    print(*[''.join(i) for i in combinations(sorted(STRING),numberOfCombinations)],sep='\n')