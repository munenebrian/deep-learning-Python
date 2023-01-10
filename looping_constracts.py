str = 'looping'

for item in str: # for is the kwy word of the for loop code. item is the variable in action
     print(item) # and in is the specifier of where we want to loop over.

favorites = ['banana', 'orange', 'strawberry', 'pineapple', 'avocado']

for item in favorites:
    print("I like this fruit...", item)


for i in range(10):
    print('looping..', i)

# these are few examples of for looping in python.

count = 0
while count < len(favorites):
    print("i love..", favorites[count])
    count += 1


for i in range(100):
    print('looping..', i)
# here if we increase the range we output more lines 
