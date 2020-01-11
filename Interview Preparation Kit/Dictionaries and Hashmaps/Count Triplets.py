
from collections import defaultdict

def countTriplets(arr, r):
    
    mp3 = {}
    mp2 = {}
    
    mp3 = defaultdict(lambda:0,mp3)
    mp2 = defaultdict(lambda:0,mp2)
    
    result = 0
    
    for element in arr:
        
        if element in mp3:
            result +=  mp3[element]
            
        if element in mp2:
            mp3[element*r] += mp2[element]
            
        mp2[element*r] += 1
        
    return result

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    
    print(ans)
