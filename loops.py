# Python For Loops

# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break Statement
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
    print(x)

# We can also set the starting value of the range() function:
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Nested Loops

adj = ["red", "big", "tasty"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement
for x in [0, 1, 2]:
    pass
# Here is the explanation about the pass statement:
# The pass statement is a null statement that is used to avoid getting an error when empty code is not allowed.
# The continue statement is used to skip the current block and return to the "for" statement.