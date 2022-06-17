from datetime import datetime
def my_decorator(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


@my_decorator
def say_bark():
    print("whoff")


say_whee()
say_bark()