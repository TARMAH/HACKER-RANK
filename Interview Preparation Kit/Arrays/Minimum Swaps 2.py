n = int(input())

arr = list(map(int, input().rstrip().split()))

def minimumSwaps(arr):
    
    i = 0
    swaps= 0
    
    while i < len(arr):
        
        if arr[i] == i+1:
            i+=1
            
        else:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps+=1
            
    print(swaps)

minimumSwaps(arr)