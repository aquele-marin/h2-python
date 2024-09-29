# Python Functions

# Creating a Function
def my_function():
    print("Hello from a function")

# Calling a Function
my_function()

# Arguments
# Information can be passed into functions as arguments.

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments
# By default, a function must be called with the correct number of arguments.

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*args):
    print("The youngest child is " + args[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Positional Only Arguments
# If you want to make a parameter positional-only, you can use / in the function definition.
# This way the parameter can't be passed by keyword.

def my_function(x, y, /):
    print(x + y)

my_function(1, 2) # you cant use my_function(x=1, y=2)

# Keyword-Only Arguments
# If you want to make a parameter keyword-only, you can use * in the function definition.

def my_function(*, country):
    print("I am from " + country)

my_function(country = "Sweden")

# Combine Positional-Only and Keyword-Only Arguments

def my_function(x, y, /, z, *, a):
    print(x + y + z + a)

my_function(1, 2, 3, a = 4)

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)





