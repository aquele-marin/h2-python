#  Python Dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"]) # Output: Ford

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
print(len(thisdict)) # Output: 3

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:

thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict) # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Access Items
# There is also a method called get()
thisdict.get("model") # Output: Mustang

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
thisdict.keys() # Output: dict_keys(['brand', 'model', 'year'])

# The keys method return a pointer to the original dictionary, adding a new item will update de list as well
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) # Output: dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) # Output: dict_keys(['brand', 'model', 'year', 'color'])

# Get Values
# The values() method will return a list of all the values in the dictionary.

x = thisdict.values()

# It's also a view of the dictionary, it will update as the dictionary is updated just like keys()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) # Output: dict_values(['Ford', 'Mustang', 1964])

car["color"] = "white"

print(x) # Output: dict_values(['Ford', 'Mustang', 1964, 'white'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()

# The returned list is a view of the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "white"

print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

