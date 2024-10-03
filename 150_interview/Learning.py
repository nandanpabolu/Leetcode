def printisokay():
    s = "Hello world"
    print(s)
    print(s[::-1])
    if s == s[::-1]:
        print ("true")
    else:
        print("false")
