from collections import defaultdict

def ransom_note(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word]+=1
    for word in ransom: 
        if dicty[word]==0 : return "No" 
        dicty[word]-=1
    return "Yes"


if __name__ == '__main__':
    
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()
    

    print(ransom_note(magazine, note))
