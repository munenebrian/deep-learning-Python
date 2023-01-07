# for the mathematical operators in python we have the addition, subtraction, division and multiplication.
print(2+3) #addition
print(2-3) #subtraction
print(2*3) #multiplication
print(2/3) #division
print(2**3) #exponentiation
print(2**-3) #exponentiation
print(2<<3) #left shift

# logical operators in python are used in conditional statements to determine a truth or false outcome
# we have and, or and not. and is used to check for both conditions to be true. or checks for at least one condtion to be true while not returns fase for a true condition.
# we have to combine them with conditional statements to make them make sense
a = True
b = True
if a and b:
    print("All true!") # this is an example of how we use the and logical operator

x = True
y = False
if x or y:
    print("One must be true!") # this is an example of how we use the or logical operator

w = False
z = False
if not(w) or not(z):
    print("Neither is false!")

