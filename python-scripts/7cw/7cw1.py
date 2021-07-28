t= list(input().split())
i = 0

print(t[-1])

for x in range(0, len(t)):
    if int(t[x]) > 0:
        i+=1
print(i)