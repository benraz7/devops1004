my_name = ["adi", "ben", "noam", "arthur", "john"]
for name in my_name:
    print(f"hello {name}")
for i in range(1, 6):
    print(f"hello world + #{i}")
    break
else:
    print("printed all names")

for i in range(len(my_name)):
    my_name[i] = "moshe"
    print(my_name[i])
a = 0
while a < 5:
    print(a)
    a = a + 1

l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")
print(l)


n = [1, 2, 3, 4, 5]
result = [num * 2 for num in n if num > 2]
print(result)

