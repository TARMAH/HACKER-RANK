
def check(s1, s2):
    
    lcDict= {}
    
    for l in s1:
        if l in lcDict:
            lcDict[l] +=1
        else:
            lcDict[l]= 1
    
    for l in s2:
        
        if l in lcDict:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    
    for _ in range(int(input())):
        
        print(check(input(),input()))