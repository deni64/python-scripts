t= list(input().split())
i = 0
for x in range(1, len(t)):
    if (int(t[x])* int(t[x-1]))>0:
        i +=1

print(i)