value = 3

t_lower = 1
t_upper = 3

block_number = 1 # TELLS WHICH BLOCK NUMBER WE ARE IN 

t = int(input())

while True:
    
    if (t_lower <= t <= t_upper):
        break
    
    #KEEP UPDATING THE BLOCK NUMBER AND LIMITS UNTIL WE REACH BETWEEN THE LIMITS
    
    block_number = block_number + 1
    t_lower = t_upper + 1
    t_upper = (t_upper *2 )+ 3


# UPDATE THE LOWER LIMIT 
lower_value = value *(2**(block_number-1)) 


#ANSWER IS EQUAL TO  LOWER VALUE - (TIME - LOWER LIMIT TIME)   

print(lower_value - (t-t_lower))
