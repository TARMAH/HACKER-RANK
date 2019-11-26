SET = set()

def isPalindrome(n):
    return str(n)[0:3]== str(n)[3:6][::-1]

def generatePalindromes():
    
    I = 100
    
    while I < 1000:
        
        J = 100000//I
        
        while J < 1000:
            
            if isPalindrome(I*J):
                SET.add(I*J)
            
            J= J+1
        I = I +1
        
generatePalindromes()
SET = list(sorted(SET))

answer = SET[0]

for _ in range(int(input())):
    
    N = int(input())

    for element in SET:

        if element >= N:
            print(answer)
            break

        answer = element