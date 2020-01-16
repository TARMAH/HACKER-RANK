def triplets(a, b, c):
    
    a = set(a)
    b = set(b)
    c = set(c)
    
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)
    
    total = 0 
    length_of_a = len(a)
    length_of_c = len(c)
    ia = 0
    ic = 0
    ta = 0 
    tc = 0
    
    for element in b:

        while ia<length_of_a and a[ia] <= element:
            ia += 1
            ta += 1
            
        while ic<length_of_c and c[ic] <= element:
            
            ic += 1
            tc += 1   
            
        total += (ta * tc )
        
    return total
        

if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    
    print(ans)