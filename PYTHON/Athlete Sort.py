N,_ = map(int,input().split())

LIST = []

for i in range(N):
    l = []
    l = list(map(int,input().split()))
    LIST.append(l)

index  = int(input())

LIST = sorted(LIST, key=lambda t : t[index])

for part in LIST:
    print(*[p for p in part])