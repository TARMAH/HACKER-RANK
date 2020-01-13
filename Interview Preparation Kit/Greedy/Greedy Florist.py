def getMinimumCost(k, c):
    
    c = sorted(c,reverse = True)
    
    customers = [1 for _ in range(k)]
    
    pointer = 0
    
    total = 0
    
    for flower_cost in c:
        
        total += ( customers[pointer] * flower_cost )
        
        customers[pointer] += 1
        
        pointer += 1
        pointer = pointer % k
    
    return total

if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    
    print(minimumCost)