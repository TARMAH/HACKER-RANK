# Complete the gridSearch function below.
def gridSearch(C,c,R,r,PATTERN,PATTERN_TO_SEARCH):
    
    row_no = 0
    r_no_pattern = 0 
    match = 0
    
    for ROWS  in range(0,int(R)-int(r)+1):
    
        for COLS in range(0,int(C)-int(c)+1):
            
            for test_row in range(row_no,row_no + r):
                
                if (PATTERN[test_row][COLS:COLS+c] != PATTERN_TO_SEARCH[r_no_pattern]):
                    break
                else:
                    match = match + 1
                    
                r_no_pattern = r_no_pattern + 1
                    
            if match == r:
                return 'YES'
                
            match = 0 
            
            r_no_pattern = 0 
            
        row_no = row_no + 1
        
    return('NO')

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        answer = gridSearch(C,c,R,r,G,P)
        print(answer)
