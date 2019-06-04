def main():
    N = int(input())
    List = []
    
    for _ in range(N):
        Query = input()
        if Query=="print":
            print(List)
        elif Query.startswith('insert'):
            _, *line = Query.split()
            numbers = list(map(int, line))
            List.insert(numbers[0], numbers[1])
        elif Query.startswith('remove'):
            _,number = Query.split()
            List.remove(int(number))
        elif Query=="sort":
            List.sort()
        elif Query.startswith('append'):
            _,number = Query.split()
            List.append(int(number))
        elif Query=="pop":
            List.pop()
        elif Query=="reverse":
            List.reverse()
            
            
        

if __name__== "__main__":
    main()


