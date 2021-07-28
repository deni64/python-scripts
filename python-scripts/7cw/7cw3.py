t= [int(i) for i in input().split()]
max = 0
for x in range(1, len(t)):
    if t[x]>t[max]:
        max = x

print(t[max])