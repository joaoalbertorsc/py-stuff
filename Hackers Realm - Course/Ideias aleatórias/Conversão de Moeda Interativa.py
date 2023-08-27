myBool = True
n = int(input("Insira um número:"))
test = n - 1
while test > 1:
    if n % test == 0:
        myBool = False
    test -= 1
print(myBool)