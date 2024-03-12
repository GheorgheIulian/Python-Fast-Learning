"""
Variable Rules
        Var names are case sensitive (name and NAME are different variables
        Must start with a letter or and _
        Can have numbers but not start with one
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str / String
is_Cool = True  # Bool

# Multiple Assigments

aNumber, bFloat, cString, dBoolean = (1,2.5,'John',False)
print(x,y,name,is_Cool,aNumber,bFloat,cString,dBoolean)

# Casting

x = str(x)
y = str(y)

print(type(x),x,type(y),y)
