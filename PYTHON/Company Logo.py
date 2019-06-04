import string

d = dict.fromkeys(string.ascii_lowercase, 0)

STRING  = input()

for alpha in STRING:
    d[alpha] = STRING.count(alpha)

d = sorted(d.items() , key=lambda t : t[1], reverse=True)[:3]

for key, val in d:
    print(key,val)