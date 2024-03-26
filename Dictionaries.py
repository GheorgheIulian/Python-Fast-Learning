# A Dictionary is a collection which is unordered , changeable  and indexed. No duplicates members allowed
# In dictionaries is using K,V (Key Value) syntax
 
# Create a dictionary
person = {
    'first_name':'John',
    'last_name':'Doe',
    'age': 37
}
print(person, type(person))

# Create a dictionary by using a constructor
person2 = dict(first_name = 'Sarah', last_name = 'James')
# print(type(person2),person2)

# Add Key/Value , get dict key, get dict values,get dict items
person['phone'] = '555-5555-4444'
print(person.keys())
print(person.values())
print(person.items())

# Copy dict
person3 = person.copy()
print(person3.items())

# Remove item from dict
del(person['age'])
person.pop('phone')
print(person.items())

# List of dictionaries
people =[
    {'name':'Martha','age':30},
    {'name':'Kevin', 'age':25}
]
print(people[1]['age'])