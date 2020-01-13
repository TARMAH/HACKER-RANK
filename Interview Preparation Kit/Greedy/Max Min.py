# Complete the maxMin function below.
def maxMin(k, arr):
    
    arr = sorted(arr)
    Min = float('inf')
    
    i = 0
    
    while k < len(arr)+1:
        
        diff = arr[k-1]-arr[i]
        
        if diff < Min:
            Min = diff
        i+=1
        k+=1
        
    return Min

if __name__ == '__main__':

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    
    print(result)
