def isValid(s):
    
    
    if len(s) == 0:
        return "NO"
    if len(s) <= 3:
        return "YES"
    
    letters = [0 for i in range(26)]
    
    for letter in s:
        letters[ord(letter)%97]+= 1
    
    letters = sorted(letters)
    
    i=0;
    while letters[i]==0:
        i+= 1;
    
    Min = letters[i]   #the smallest frequency of some letter
    Max = letters[25]  #the largest frequency of some letter
    
    valid = "NO"
    
    if (Min == Max):
        valid = "YES"
    else:
        if(((Max - Min == 1) and (Max > letters[24])) or
            (Min == 1) and (letters[i+1] == Max)):
            valid = "YES"
            
    return valid

s = input()

print(isValid(s))