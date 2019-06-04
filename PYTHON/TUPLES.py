def main():
    N = int(input())
    input_line = input()
    input_list = input_line.split()
    input_list = map(int, input_list)
    t = tuple(input_list)
    print(hash(t))
        

if __name__== "__main__":
    main()