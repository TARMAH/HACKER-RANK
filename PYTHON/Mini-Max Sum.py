def main():
    input_line = input()
    input_list = input_line.split()
    input_list = list(map(int, input_list))

    MAX = -1
    MIN = 10000000000000000000000000000
    
    for i in range(5):
        SUM = sum(input_list[0:i]+input_list[i+1:])
        if SUM>MAX:
            MAX = SUM
        if SUM<MIN:
            MIN = SUM

    print(MIN,MAX)

if __name__== "__main__":
    main()