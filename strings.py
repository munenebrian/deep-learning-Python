# with strings we have multi line strings and single line strings.
varA = "This is a car" #single string
print(varA)
varB = "This is a long sentence" \
    "and we trying to break it" \
        "because we know how" #multi string
print(varB)
# key to note and remember, a string is like an array in that we can acces every element of the string by their indexing
name = 'Brian'
print(name)
print(name[0])
# built in functions in python
# we have the print() function it outputs anything put in it.
# we have the input() function.
print("Where do you live?")
location = input()
print("So you live in " + location + "!")
# we also have len() which gives us the lenght value of the variable
# str() this converts to a string int() converts to a integer float() converts to a float value
# when Python runs operations involving integers and floats, it implicitly converts the integers type to a float, and then completes the operation.
