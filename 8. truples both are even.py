coordinates= [(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]
l=[]
for a,b in coordinates:
    if a%2==0 and b%2==0:
        l.append((a,b))
print(l)