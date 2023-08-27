# Tuples in Python
t = (1, 2.0, "hacker", True)
print(t)

t = 1, 2, 3
print(t)

# immutable
# [0] = 4
# print(t)

# access the tuples
# index
print(t[2])

# access from reverse
print(t[-1])

# slicing
print(t[1:3])

# reverse
print(t[::-1])

# delete element
# del t[0]
# print(t)

# delete entire tuple
del t

# basic operation in tuple
t = 1, 2, 3, 4

# legth
print(len(t))

t2 = 5, 6, 7

# concatenate
t = t + t2
print(t)

# repeat numbers
temp = (0,) * 5
print(temp)
l = [1, 2, 3, 4, 5]

# convert list to tuple
t = tuple(l)
print(t)
