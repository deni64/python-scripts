a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = a-c
i = b-d
if k<0:
    k= -k
if i<0:
    i= -i
if (b==d) or a==c or k==i:
    print('ферзь сможет побить фигуру')
else:
    print('ферзь не сможет побить фигуру')