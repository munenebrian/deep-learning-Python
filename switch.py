# in the instance of numerous conditions, we use match statements instead of if statements.
# this is new to python and was introduced by version 3.10
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
