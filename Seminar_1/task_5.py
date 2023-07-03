e = 3
n = 10
i = 1
sum = 0
while i <= n:
    if i % 2 == 0 and i % e != 0:
        sum += i
    i += 1
print(sum)