try:
    a = 10
    b = 0
    print(a / b)
    r = open("file_not_exists")
except ZeroDivisionError:
    print("could not divide by 0")
except FileNotFoundError:
    print("could not find file")
print("blabla")
