print('while loop:')
# print from 1 to 10
num = 1
while num <= 10:
    print(num)
    num += 1
print()

# for loop
print('for loop:')
for num in range(1, 11, 1):
    print(num)
print()

# print odd numbers
print('print odd numbers:')
for num in range(1, 11, 2):
    print(num)
print()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        print(mat[i][j])
print()

for i in range(3):
    for j in range(3):
        print(mat[i][j], end=" ")
    print()

# break
print('break:')
for i in range(10):
    print(i)
    if i == 5:
        break

# continue
print('continue')
for i in range(10):
    if i % 2 == 1:
        continue
    print(i)

# pass
print('pass:')
for i in range(10):
    pass

def fun():
    pass