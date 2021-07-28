i=list(input().split())
min=1000
for k in range(len(i)):
    x=int(i[k])
    if (x<min)and(x>0):
        min=x
print(min)