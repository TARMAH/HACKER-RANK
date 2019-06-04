from collections import OrderedDict

ordered_dictionary = OrderedDict()

N = int(input())

for _ in range(N):
    
    INPUT = input()
    
    *key, value = INPUT.split()
    
    KEY = ' '.join(key) 
    
    if KEY not in ordered_dictionary:
        
        ordered_dictionary[KEY] = int(value)
    
    else:
        
        ordered_dictionary[KEY] = ordered_dictionary[KEY] + int(value)
    
for key, value in ordered_dictionary.items():
    print(key,value)