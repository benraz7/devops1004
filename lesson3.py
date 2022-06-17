# try:
#     a = 1 / 0
# except ZeroDivisionError:
#     print("Division by zero is forbidden")


# try:
#     x = 1
# finally:
#     print("finally")


def write_to_file(name, content, mode="a", encoding="utf8"):
    with open(name, mode, encoding=encoding) as f:
        print(content, file=f)


def print_file(name, encoding="utf8"):
    with open(name, "r", encoding=encoding) as f:
        print(f.read())


write_to_file("words.txt", "Ben", "w")
print_file("words.txt")
write_to_file("words.txt", "בן")
print_file("words.txt")


# 11
# from PIL import Image
#
# width = 400
# height = 300
# image = Image.new(mode="RGB", size=(width, height))
# image.show()
