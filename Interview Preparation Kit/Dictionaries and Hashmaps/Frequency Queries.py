from collections import defaultdict

def printDict(d):
    
    for key, value in d.items():
        print(key , " ",value)
    print()

def freqQuery(queries):
    
    frequency_dict = {} #Stores number of numbers with a specific frequency
    number_dict = {}  #Stores each numbers's frequency
    
    
    frequency_dict = defaultdict(lambda:0,frequency_dict)
    number_dict = defaultdict(lambda:0,number_dict)
    
    for query in queries:
        
        if query[0] == 1:
            
            frequency_dict[ number_dict[ query[1] ] ] -=  1
            number_dict[ query[1] ] += 1
            frequency_dict[ number_dict[ query[1] ] ] +=  1
            
        elif query[0] == 2:
            
            if number_dict[ query[1]] > 0:
                
                value = number_dict[ query[1] ] 
                number_dict[ query[1] ] -= 1
                frequency_dict[value] -= 1
                frequency_dict[ number_dict[ query[1] ] ] += 1
        
        else:
            
            if frequency_dict[ query[1] ] > 0:
                print("1")
            else:
                print("0")
                
        
        
if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    ans = freqQuery(queries)
