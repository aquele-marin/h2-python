# Python Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Example
x = lambda a : a + 10
print(x(5))

# Why use lambda functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.