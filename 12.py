# my_file = open("url.txt")
# for line in my_file.readlines():
#     print(line, end='')


my_file = open("name.txt", "w")
for i in range(5):
    current_name = input("enter your name: ")
    my_file.write(f"{current_name}\n")


my_file.close()


