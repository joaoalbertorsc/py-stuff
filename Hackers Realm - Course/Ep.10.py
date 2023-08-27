l = [1, 2.0, "hacker", True]
print(l)

# how the list grows dynamically
2, 4, 8, 16, 32, 64, ...

# access the list
# index
print(l[0])
print(l[2])

# use negative index to acces from REVERSE
print(l[-1])
print(l[-3])

# slicing
print(l[1:])
print(l[1:3])

# reverse
print(l[::-1])

# update
l[3] = "aswin"
print(l)

# delete
del l[3]
print(l)

# basic operations
# length
print(len(l))

# concatenate
l2 = [4, 5, True]
l = l + l2
print(l)

# repeat certain values
l2 = [0] * 10
print(l2)

# iterate values from list
for i in l:
    print(i)

# iterate two or more list
for i, j in zip(l, l2):
    print(i, j)

# list function
l = [1, 2, 3, 4, 5, 6]

# minimum
print(min(l))
print(max(l))

# list conversion
temp = list("hackershelm")
print(temp)

# add a new element at the END
print(l.append(10))

# remove from the end
t = l.pop()
print(t, l)

# extend list
print(l.extend(temp))

# count
print(l.count("a"))

# find index od element
print(l.index(6))

# insert new element at certain index
print(l.insert(5, 7))

# remove element
l.remove('r')
print(l)

# reversing the list
l.reverse()
print(l)

# sort
print(temp.sort())

# sorting reverse
print(temp.sort(reverse=True))

t = sorted(temp)
print(t)
print(temp)

# list comprehension
temp = [0 for i in range(5)]
print(temp)

temp = [i for i in range(5)]
print(temp)

mat = [[] for i in range(3)]
print(mat)

mat = [[0 for j in range(3)] for i in range(3)]
print(mat)

for row in mat:
    print(*row)
