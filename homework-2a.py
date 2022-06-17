# Second Class HomeWork
# A
x = 3
y = 2
if x > y:
    print("BIG")
else:
    print("Small")

# B
for num in range(5):
    print(num)

# C
a = 1
if a == 1:
    print("summer")
elif a == 2:
    print("winter")
elif a == 3:
    print("fall")
elif a == 4:
    print("spring")

# D - Answer is 10 Times
count = 1
while count < 11:
    print(count)
    count = count + 1

# E
age = 32
first_letter = "B"
current_shekel_dollar = 3.3
did_you_flew_abroad = True
your_apartment_number = 43

print(age)
print(first_letter)
print(current_shekel_dollar)
print(did_you_flew_abroad)
print(your_apartment_number)
print(current_shekel_dollar + age)

# F
print("Please enter your phone number")
phone_number = int(input())
print(f"phone number {phone_number}")


# G
def printhello():
    print("hello")


def calculate():
    print(5 + 3.2)


# H
def receive_name(name):
    print(name)


def receive_number(number):
    number = number / 2
    print(number)


# I
def sum_of_two_number(num1, num2):
    sum1 = num1 + num2
    return sum1


def two_strings(str1, str2):
    str3 = f"{str1} {str2}"
    return str3


# K
N = 5
z = "#"
for x in range(N):
    for y in range(1):
        print(z)
    z = z + "#"

# L
N = 7

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j - 1) == i):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


# M
def get_number():
    number = int(input())
    return number


def compute_sum():
    sum_of_digits = 0
    for digit in str(get_number()):
        sum_of_digits += int(digit)
    return sum_of_digits
