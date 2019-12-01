def generatePrimes(): 
    
    prime = [True for i in range(1000000+1)] 
    
    p = 2
    
    while (p * p <= 1000000): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, 1000000+1, p): 
                prime[i] = False
        p += 1
        
    
    SUMS = [0 for i in range(1000000+1)]
    
    sum2 = 0
    for p in range(2, 1000000+1): 
        if prime[p]:
            sum2+=p
            
        SUMS[p]=sum2
            
    return SUMS


SUMS =  generatePrimes()

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if(n<2):
        print(0)
        continue
    if(n==2):
        print(2)
        continue
    print(SUMS[n])