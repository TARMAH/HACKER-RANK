def mutate_string(string, position, character):
    string = string[:int(i)]+character+string[int(i)+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)