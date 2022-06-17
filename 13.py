import requests


def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is OK")


def add_name():
    my_file = open("name.txt", "a")
    current_name = input("enter your name: ")
    my_file.write(f"{current_name}\n")


def hello_name_from_file():
    with open("name.txt") as my_file:
        for line in my_file.readlines():
            print(f"hello {line}", end='')


def call_urls():
    with open("url.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())


call_urls()
add_name()
hello_name_from_file()
