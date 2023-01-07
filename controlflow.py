# control flow is the order in which instructions in a program are being executed.
# let us create an if statement
weight = int(input("Your weight is? "))

gravity = 8
ave_weight = 72
over_weight = 128

if weight >= ave_weight and weight <= over_weight:
    print("You are above average weight and not overweight ")
    weight = weight - gravity
elif weight > over_weight:
    print("You are overweight ")
    weight = weight - gravity
else:
    print("You are below average weight and ")
    weight = weight - gravity

print("Your weight in mars is: ", weight)
