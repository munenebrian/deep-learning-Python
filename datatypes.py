#in python we have five main data types
# we have Numeric, Sequence, Dictionary, Boolean and Set
# for the numeric type we have three subcategories, these are intergers, floats and complex numbers
# for the sequence type we have three subcategories, these are lists, tuples and strings.
# #Tuples are similar to strings only that you can not change values in a tuple whreas you can change values in a string.
# for the dictionary type we store values in a key value object structure, we could store any data type inside a dictionary.
# for the boolean type we have two subcategories, integers and strings
# for the set type we have two subcategories, integers and strings
x = 45 # integer
print(type(x))
y = 10 + 10j #complex number
print(type(y))
a = 4.5 #float value
print(type(a))
b = "hello" #string value
print(type(b))
c = [1,2,3] #list value
print(type(c))
d = {'a':1,'b':2,'c':3} #dictionary value
print(type(d))
e = ('A', 34, 'f', 2) #tuple
print(type(e))

print(type(False)) #any truthy or falsey value is a boolean
