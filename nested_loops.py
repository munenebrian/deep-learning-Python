list1 =[1,2,3,4,5,6,7,8,9]
list2 =[1,2,3,4,5,6,7,8,9]

count = 0
# outer loop
for x in list1 :
    count += 1
    # inner loop
    for y in list2 :
        count += 1

print(count)
