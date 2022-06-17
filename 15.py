def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age can not be negative")


a = input("enter number: ")


def check_my_number(num):
    try:
        a = int(num)
    except ValueError:
        return False


try:
    get_age()
except Exception as e:
    print(e.args)
