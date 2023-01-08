# in the instance of numerous conditions, we use match statements instead of if statements.
# this is new to python and was introduced by version 3.10
# we are using version 3.8.10 and does not allow match here, so we are can compare if elsenand elif on how the work as to match.
     # an example of if, else and elif
http_status = 550

if http_status == 200 or http_status == 201:
    print("Success")
elif http_status == 400:
    print("Bad Request")
elif http_status == 404:
    print("Not Found")
elif http_status == 500 or http_status == 501:
    print("Internal Server Error")
else:
    print("Unknown Error")

  # an example of match
http_status = 200

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Not found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")
