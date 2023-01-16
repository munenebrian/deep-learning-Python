num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# this prints all numbers in the list
for num in num_list:
    print(num)

# this prints numbers greater than 45
for num in num_list:
    if num > 45:
        print(num)

# this prints a statement to all avlues in the list, whether over or under 45
for num in num_list:
    if num > 45:
        print('Over 45')
    else:
        print('Under 45')

# this prints exactly where a specific value is in the string
for x,num in enumerate(num_list):
    if num == 36:
        print('Number found at ', x)

# this prints
count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)

print(count)

# this prints
count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)
