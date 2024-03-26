# A Tupple is a collection  wich is ordered and unchangeable also allows duplicate members. 

# Create tuple
fruits = ('Apple', 'Oranges','Mini','Beans', 5)
print(type(fruits), fruits)


# A Set is a collection which  is unordered and unindexed does not accpet duplicate members

# Create a Set
fruits_set = {'Apple','Orange','Mango'}
print(type(fruits_set),fruits_set)

# Check if a value is in a set
print('Apple' in fruits_set) # return Boolean value

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

