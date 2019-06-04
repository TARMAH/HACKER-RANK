from itertools import product

K,M = input().split()

LIST = []

#APPENDING ALL LISTS INTO A LIST 

for _ in range(int(K)):
    current_list = list(map(int,input().split()))
    LIST.append(current_list[1:])

# TAKING PRODUCT

PRODUCTS = list(product(*LIST))

#TAKING SUM OF SQUARE OF EACH ALL LISTS in LIST

NEW = [sum(map(lambda i : i * i, PRODUCT)) for PRODUCT in PRODUCTS  ]

#TAKING MOD BY M

NEW = list([i % int(M) for i in NEW])

#PRINTING THE MAXIMUM VALUE

print(max(NEW))