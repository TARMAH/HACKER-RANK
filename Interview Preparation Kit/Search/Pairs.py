
# Complete the pairs function below.
def pairs(k, arr):
    
    LIST = {}
    count = 0
    
    for element in arr:
        
        if element in LIST:
            count+=1
        else:
            LIST[element] = 1
            
        if element+k in LIST:
            count+=1
        else:
            LIST[element+k] = 1
        
    return count

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
    
    print(result)
