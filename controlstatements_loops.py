#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break
else:
    print('No sorry, not a dessert on my list')
# The break statement is used to stop the loop, which in turn also stops the else condition. Without the break the loop will continue even after the if condition is satisfied.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

# Similar to break, continue can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)

# The pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.
