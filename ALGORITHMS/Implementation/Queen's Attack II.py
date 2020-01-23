ll = lambda: list(map(int,input().split()))
n,k = ll()
rq,cq = ll()
num_moves = [n-cq, min(n-cq,rq-1), rq-1, min(rq-1,cq-1), cq-1, min(cq-1,n-rq), n-rq, min(n-rq, n-cq)]
for a0 in range(k):
    ro,co = ll()
    if ro==rq:
        if co>cq: num_moves[0]=min(num_moves[0],co-cq-1)
        else: num_moves[4]=min(num_moves[4],cq-co-1)
    elif co==cq:
        if ro>rq: num_moves[6]=min(num_moves[6],ro-rq-1)
        else: num_moves[2]=min(num_moves[2],rq-ro-1)
    elif ro-rq==co-cq:
        if ro-rq>0: num_moves[7]=min(num_moves[7],ro-rq-1)
        else: num_moves[3]=min(num_moves[3],rq-ro-1)
    elif ro-rq==cq-co:
        if ro-rq>0: num_moves[5]=min(num_moves[5],ro-rq-1)
        else: num_moves[1]=min(num_moves[1],rq-ro-1)
print(sum(num_moves))