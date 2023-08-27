string = 'hello'
print(string)

string = string + ' world'
print(string)

string = "H" + string[1:]
print(string)

# string manipulation
var = "gamer"
print("%s is the best" % (var))
print(string[:5])
print(string[6:])
print(string[3:6])

# reverse
print(string[::-1])
print(string[::3])

# STRING FUNCTIONS

# length (num of characters)
print(len(string))

# count
print(string.count("o"))

# find
print(string.find("world"))

# index
print(string.index("l"))

# use r to find from REVERSE
print(string.rindex("l"))

# lowercase
print(string.lower())

# uppercase
print(string.upper())

# replace
print(string.replace('world', 'users'))

# split
print(string.split(" "))

# swap-case
print(string.swapcase())

# string formatting
print(string.center(30, "$"))

print(string.ljust(30, "#"))

print(string.rjust(30, "&"))