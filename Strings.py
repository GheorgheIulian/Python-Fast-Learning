#String in python are surrounded by either  single or double quotation marks.

name = "Brad"
age = 37

# Concatenate

print ("Hello my name is " + name + "and i am "  + str(age)) # Casting required for int var

# String Formating
    # Arguments by position
print ("My name is {name} and i am {age}".format(name=name, age = age))
    # F-Strings
print (f"My name is {name} and i am {age}")

# String Methods

s = "hello world!"

# Capitalize string 
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())