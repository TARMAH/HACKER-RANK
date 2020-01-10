def num_of_ways(n):
    
    if n == 0 : 
        return 1
    
    nums = [None for i in range(n+1)]
    nums[0] = 1
    
    for i in range(1,n+1):
        total = 0 
        for step in [1,2,3]:
            if i-step >= 0:
                total += nums[i-step]
        nums[i] = total
    
    return nums[n]

for _ in range(int(input())):
    n = int(input())
    print(num_of_ways(n))


### reference Material https://youtu.be/5o-kdjv7FD0