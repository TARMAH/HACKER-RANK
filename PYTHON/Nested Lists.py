if __name__ == '__main__':
    List = []
    number = int(input())
    for _ in range(number):
        name = input()
        score = float(input())
        smallerlist=[]
        smallerlist.append(name)
        smallerlist.append(score)
        List.append(smallerlist)
        
    MIN=min(List, key=lambda x: x[1])[1]
    
    List = sorted(List, key=lambda x: x[1])
    List = [element for element in List if MIN not in element] 

    MIN=min(List, key=lambda x: x[1])[1]

    L = [element[0] for element in List if MIN in element]
    L.sort()

    for element in L:
        print(element)
