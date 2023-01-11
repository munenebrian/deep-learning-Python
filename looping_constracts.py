str = 'looping'

for item in str: # for is the kwy word of the for loop code. item is the variable in action
     print(item) # and in is the specifier of where we want to loop over.

favorites = ['banana', 'orange', 'strawberry', 'pineapple', 'avocado']

for item in favorites:
    print("I like this fruit...", item)
# the for loop makes it easy to work withany type of sequence in python.
# in the code above, for loop iterates through the listed items in the array
for i in range(10):
    print('looping..', i)

# these are few examples of for looping in python.

count = 0
while count < len(favorites):
    print("i love..", favorites[count])
    count += 1
#  a while loop is based upon a condition to being true, once the condition is no longer true the loop stops executing
# a while loop needs a counter variable to be checked in with the condition.

for i in range(100):
    print('looping..', i)
# here if we increase the range we output more lines

# in this next code we want to isolate one item in our list of desserts

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)
else:
    print('No sorry, that dessert is not on my list')
