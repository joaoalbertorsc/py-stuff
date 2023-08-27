# basic data types
print('Basic data types:')
a = 1       # integer
b = 2.0     # float
c = "ash"       # string
print(a, b, c)
print()

# multiple assigment
print('Multiple assigment:')
a = b = c = d = 0
print(a, b, c, d)
a, b, c = 1, 2.0, "ash"
print(a, b, c)
print()

# String
print('String:')
s = "hackers Realms"    # immutable
print(s[0])
print(s[0:7])   # it will print the word in index range ([0:7] or [:7])
print(s[:7])
print(s[8:])    # print from 8th index to the end of the string ([8:])
print(s * 3)    # multiply the string 3 times
print(s + " channel")
print()

print(s + ' Biruleibe')
print()

# list - put more thatn one thing in the same var
print('List:')
var0 = [1, 3.0, 'GOKU']
print(var0)
print(var0[0])  # first element
var0[0] = 2 # mutable
print(var0)
var1 = [1,2,3,4,5]
newlist = var0 + var1   # concatenate
print(newlist)
print()

# tuples same as list but
# immutable
tup = (1, 5.0, True, "str")
print(tup)
print()

# dictionary - hashmap
print('Dictionary - hashmap:')
# key: value
d1 = {1: "one", "ten": 10}
print(d1)
print(d1[1])    # print value for 1
print(d1["ten"])
print(d1.keys())
print(d1.values())  # print the values
print()

# data type conversion
print('Data type conversion:')
a = 2.0
print(type(a))
print()

a = int(a)      # float to into
print(type(a))
print()

a = str(a)      #int to string
print(type(a))
print(a)
print()

# set - unique values
print('Set - unique values:')
s = {1,1,2,2,3}
print(s)
print()

# ascii char
print('Ascii char:')     # char "number" (número que o caractere representa no reclado)
print(ord("a"))     # char to int

print(chr(200))
print(chr(26))
print(chr(50))

help()