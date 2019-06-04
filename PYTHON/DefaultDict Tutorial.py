from collections import defaultdict

n,m = map(int,input().split())

word_indexes = defaultdict(list)

L =[]

#storing all words of  A in dictionary

for _ in range(n):
    L.append(input())

#storing all words of B in dictionary
words = []

for i in range(m):
    word = input()
    words.append(word)

#appending word indexes to dictionary
for (index, word) in enumerate(L):
    word_indexes[word].append(int(index+1))

#printing result
for word in words:
    if word in word_indexes:
        print(*word_indexes[word])
    else:
        print(-1)