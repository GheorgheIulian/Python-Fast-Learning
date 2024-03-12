# A List is a collection wich is ordered  and changeable also accpets duplicates . Allows duplicate memebers

#  Create a List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples','Oranges','Grapes','Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5,6,5))
 # print(type(numbers2),numbers2)

# Get a value
print(fruits[3])

# Get Length
print(len(fruits))

# Append to a list
fruits.append('Mango')
print(fruits)

# Remove from a list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(3,'Pineapple')
print(fruits)

# Reverse and sort
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)



