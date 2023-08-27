num = 5
# check it is positive
# if condition
if num >= 0:
    print("It is positive")

num = -5
# check it is positive or negative
# if-else condition
if num >= 0:
    print("It is positive")
else:
    print("it is negative")

num = 0
# check it is positive or negative
# if-elif-else condition
if num > 0:
    print("It is positive")
elif num < 0:
    print("it is negative")
else:
    print("it is zero")

# nested id condition
num = 150
if num > 0:
    if num > 100:
        print("greater than 100")
    else:
        print("less than 100")
else:
    print("less than zero")

# one line if condition
num = 5
string = "even" if num % 2 == 0 else "odd"
print("even" if num % 2 == 0 else "odd")

num = 10
print("even" if num % 2 == 0 else "odd")
