def commonChild(s1, s2):
    
    LIST = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    
    Max = 0
    
    for i in range(1,len(s1)+1):
        
        for j in range(1,len(s2)+1):
            
            if s1[i-1] ==  s2[j-1]:
                LIST[i][j] = LIST[i-1][j-1] + 1
            else:
                LIST[i][j] = max([LIST[i][j-1],LIST[i-1][j] ])
                
            if LIST[i][j] > Max:
                Max = LIST[i][j]
                
    return Max

print(commonChild(input(),input()))

# for reference see this video https://www.youtube.com/watch?v=NnD96abizww