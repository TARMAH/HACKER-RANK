def checkPr(letter):
    if letter.isalpha():
        if letter.islower():
            return 1
        else:   return 2
    elif int(letter)%2==1:   return 3
    else:   return 4

word = input()
arr = sorted(word,key= lambda x: (checkPr(x),x) )
print(*arr,sep='')