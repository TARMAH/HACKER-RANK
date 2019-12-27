A = list(input())
B = list(input())

Count = [0]*26

for element in A:
    Count[ord(element)%97] += 1
    
for element in B:
    Count[ord(element)%97] -= 1
    
Count =  [abs(ele) for ele in Count] 

print(sum(Count))