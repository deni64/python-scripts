spisok = [int(i) for i in input().split()]
spisok2 = filter(lambda x: x%2==0, spisok)
print(*spisok2)