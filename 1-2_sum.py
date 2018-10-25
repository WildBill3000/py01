# 1-2 sum

a = input("Gimme a number: ")
b = input("Gimme another number: ")
a, b = map(int, [a, b])

#print(a + " + " + b + " = " + str(int(a) + int(b)))
print("Math!")

# you can do string concatenation, but it's frowned on
# in the Python world. These days, you'd want to use 'f' 
# strings or the str.format method.

print(f"{a} + {b} = {a + b}")

# this is a little tidier, and if you don't like the calls to 
# int, you can wrap the input like this:

# a = int(input("Gimme a numbe: "))

# or slightly too fancy:
# a, b = map(int, [a, b])

# why does that work?
# `map` runs a function--the first arg--on each element of a 
# list--the second arg and returns a list with two elements.
# if you assign an iterable with two elements to two variables
# the list is "destructured" automatically