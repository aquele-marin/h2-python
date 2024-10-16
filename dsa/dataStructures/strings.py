# Python Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello")
print('Hello')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings

# You can assign a multiline string to a variable by using three quotes: or three single quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

# String are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

# String Length

print(len(a))

# Check String
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

# use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if is not present:
print("expensive" not in txt)

# Python - Slicing Strings

# You can return a range of characters by using the slice syntax.

b = "Hello, World!"
print(b[2:5])

# Slice From the Start
print(b[:5])

# Slice To the End
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print(b[-5:-2])

# Modify Strings
# Upper Case
print(b.upper())

# Lower Case
print(b.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())

# Replace String
print(b.replace("H", "J"))

# Split String
print(b.split(",")) # returns ['Hello', ' World!']

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# but we can combine strings and numbers by using the format() method!

# F-Strings
# Python f-strings provide a way to embed expressions inside string literals, using curly braces {}.
# F-String was introduced in Python 3.6 and is now the preferred way of formatting strings.

age = 36
txt = f"My name is John, and I am {age}"
print(txt)

# A placeholder can include a modifier to format the value
price = 49
txt = f"The price is {price:.2f} dollars"
print(txt)

# Escape Character
# To insert characters that are illegal in a string, use an escape character.

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# String join() method
# The join() method takes all items in an iterable and joins them into one string.
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

# Python - String Methods
#  A list with all python's string methods can be found here: https://www.w3schools.com/python/python_strings_methods.asp