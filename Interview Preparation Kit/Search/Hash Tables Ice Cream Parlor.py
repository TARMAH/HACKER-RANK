
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    
    Dict = {}
    
    i = 1
    
    for c in cost:
        
        if c in Dict:
            
            print(Dict[c],i)
            return
            
        else:
            
            Dict[money - c] = i 
            i += 1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)