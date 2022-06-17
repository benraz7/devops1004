isTrue = False
a = 2
b = 2
c = [1, 2, 3]
d = [1, 2, 3]
if type(a) is int:
    print("a is of type int")
if a == b:
    print("a equals b")
if c == d:
    print("c equals d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")
strOne = "One"
strThree = "Three"
age = int(input("enter your age: "))
if 0 < age < 120:
    print("All good")
my_name = ["adi", "ben", "noam", "arthur"]
my_list = []
if my_name:
    print("my list is not empty")
if len(my_name) > 2:
    print("I remember enough names")
if my_list:
    print("my list is not empty")
if "zohar" not in my_name:
    print("true")
if a < b and (strThree == 3 or isTrue == 4):
    print("a is less than b")
elif a == b:
    print("a is equal b")
elif strOne != strThree:
    print("hello")
else:
    print("a is greater than b")