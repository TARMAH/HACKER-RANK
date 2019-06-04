def main():
    n = int(input())
    arr = list(set((map(int, input().split()))))
    arr.sort()
    print(arr[len(arr)-2])

if __name__== "__main__":
    main()
