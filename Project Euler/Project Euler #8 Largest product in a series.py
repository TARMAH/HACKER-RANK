def multiply(num):
    ans = 1
    for i in range(len(num)):
        
        if int(num[i]) == 0:
            return 0
            
        ans = ans * int(num[i])
        
    return ans


for _ in range(int(input())):
    
    MAX = 0
    
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    for i in range(len(num)-k+1):
        
        temp = multiply(num[i:i+k])
        
        if temp>MAX:
            MAX = temp
    
    print(MAX)