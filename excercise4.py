# import requests
#
# # 1
#
# response = requests.get("https://api.github.com/users/avielb/repos")
#
# repos_list = response.json()
# repos_set = set()
# for repo in repos_list:
#     repos_set.add(repo["name"])
# print(len(repos_set) >= 5)
#
# # 2
#
# import names
# for i in range(3):
#     name = names.get_first_name()
#     response = requests.get(f"https://api.agify.io/?name={name}")
#     names_list = response.json()
#
#     try:
#         is_in_range = (0 <= int(names_list["age"]) <= 120)
#         print(f"{name} is in range={is_in_range}")
#     except:
#         print(f"{name} not in list")
#
# # 3
#
#
# response = requests.get("http://universities.hipolabs.com/search?country=Israel")
# repos_list = response.json()
# repos_set = set()
# for repo in repos_list:
#     repos_set.add(repo["name"])
# print(len(repos_set) >= 5)

# 4
from selenium import webdriver

def title_check(my_driver):
    my_driver.get("https://www.ycombinator.com/")
    return my_driver.title

assert title_check(webdriver.Chrome()) == "Y Combinator"

# 5

from selenium import webdriver

def title_check(my_driver):
    my_driver.get("https://hub.docker.com")
    return my_driver.title

assert title_check(webdriver.Chrome()) == "Docker Hub Container Image Library | App Containerization"
