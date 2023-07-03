num = int(input("Input some number between 1 and 999: "))
res = None
# action = None
if num > 99 and num < 1000:
    res = "Its's 3 symbols, "
    num2 = 0
    while num > 0:        
        digit = num % 10
        num = num // 10
        num2 = num2 * 10 
        num2 = num2 + digit
    num = num2
elif num > 9 and num < 100:
    res = "Its's 2 symbols, "
    num = (num % 10) * (num // 10)
elif num < 10 and num > 0:
    res = "Its's 1 symbol, "
    num = num**2
else:
    res = "Input some number between 1 and 999: "
print(res, num)
