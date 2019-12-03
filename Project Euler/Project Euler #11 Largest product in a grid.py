#Append Zeros for boundry scenarios
GridCheck = []
for _ in range(26):
    grid_t = [0 for i in range(26)]
    GridCheck.append(grid_t)


#Take Input
grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

#Assign Input to Our LIST name GridCheck
for idx , row in enumerate(GridCheck[3:23]):
    row[3:23] = grid[idx]


max_sum = 0

#Check 4 cases for each number

for i in range(3,23,1):
    for j in range(3,23,1):
        
        #HORIZONTAL RIGHT
        HR = GridCheck[i][j] * GridCheck[i][j+1] * GridCheck[i][j+2] * GridCheck[i][j+3]
        
        #TOP
        TOP = GridCheck[i][j] * GridCheck[i-1][j] * GridCheck[i-2][j] * GridCheck[i-3][j]
        
        #TOP RIGHT DIAGONAL
        TRD = GridCheck[i][j] * GridCheck[i-1][j+1] * GridCheck[i-2][j+2] * GridCheck[i-3][j+3]
        
        #BOTTOM RIGHT DIAGONAL
        BRD = GridCheck[i][j] * GridCheck[i+1][j+1] * GridCheck[i+2][j+2] * GridCheck[i+3][j+3]
        
        if max(HR,TOP,TRD,BRD) > max_sum:
            max_sum = max(HR,TOP,TRD,BRD)
        
print(max_sum)
