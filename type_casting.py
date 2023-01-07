# we know what type casting is, we know the two types, implicit and explicit.
user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = int(user_num_1) + int(user_num_2)
print(user_sum)

num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
# print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum) this line here will throw an error
# why? implicityl python can convertcompatible data types, ie. float and int but not a float and string.
print("The sum of: " + str(num_1) + " and " + str(num_2) + " is " + str(user_sum))
