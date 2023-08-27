# Basic Operators in Python
print('Basic Operators in Python:')
mais = (2 + 3)       # doesnt need ()
print(mais)
menos = (10 - 5)
print(menos)
mult = (2 * 3)
print(mult)
div = (5 / 3)
print(div)
divsemfloat = (5 // 3)      # same as 5/3 but not 'float'
print(divsemfloat)

restofdiv = (6 % 4)       # rest of the '6/4'
print(restofdiv)

elevar = (2 ** 4)      # ['*' > multiplica] ['**' > eleva]
print(elevar)
print()
# comparasion operators
# return bollean values [V - F]
print('''Comparasion operators;
Return bollean values:''')
igual = (2 == 2)
dif = (2 != 2)
dif1 = (2 != 3)
maior = (5 < 10)
menor = (5 > 10)

print("", igual, """
""", dif, """
""", dif1, """
""", maior, """
""", menor)
print()

# assignment operators
print('assignment operators')
a = 1
print(a)
a += 2      # a = a + 2
print(a)
a -= 1      # a = a - 1
print(a)
a *= 3      # a = a * 3
print(a)
a /= 2      # a = a / 2
print(a)
a //= 2     # a = a // 2 (no float)
print(a)
a = 5
a %= 3      # a = a(5) % 3
print(a)
a **= 5     # a = a ** 5 [to rhe power (elevado)]
print(a)
print()

# Logical operators (TRANSFORM TO BINARIES)
print('Logical operators')
a = 5
b = 10
print("5:", bin(a))
print("10:", bin(b))

c = a & b
print(bin(c))
c = a | b
print(bin(c))
c = a ^ b
print(bin(c))

c = ~a
print(bin(c))

c = b >> 2
print(bin(c))
print()

# Logical operators (V e F)
print('Logical operators:')
loop = (True and True), \
       (True and False), \
       (True or False), \
       (not False)
print(loop)
print()

# membership operators (TRUE OR FALSE)
print('membership operators:')
meop = (2 in [1, 2, 3]), \
       (5 in [1, 2, 3]), \
       ('a' in 'abc'), \
       (5 not in [1, 2, 3]), \
       (2 not in [1, 2, 3])
print(meop)
print()

# identity operator
print('identity operator:')
iop = 'word' is 'word', \
      'wor' is 'word', \
      'word' is not 'word', \
      'word' is not 'wor',
print(iop)
