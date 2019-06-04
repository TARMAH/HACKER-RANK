from itertools import groupby

I = input()

print(*[ (  len(list(items)),int(group) )  for group, items in groupby(I)])
