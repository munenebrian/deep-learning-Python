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
# nested loops happen when a loop loops over another loop till the former is executed for the latter to end.
# this happens when the first loop is outlined and the second depends on the first one. If the first one is executed, the second one is executed.
# each condition in the first loop has to be met for the second loop to be finished
# .
import time
start_time = time.time()

 # outer loop
for i in range(100):
    #inner loop
    for j in range(100):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2))
