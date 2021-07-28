n = int(input()) # число
k = int(input()) # степень
i = 1 # текущая степень
result = 1
while i <= k:
    result *= n
    i += 1
print(result)