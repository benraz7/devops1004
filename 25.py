from selenium import webdriver

# my_driver = webdriver.Chrome(executable_path="c:/users/...")
def calculate_tip(my_driver):
    my_driver.get("c:/users/Raz-Family\Desktop/tip_calc/tip_calc/index.html")
    my_driver.find_element_by_id("billamt").send_keys("100")
    my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
    my_driver.find_element_by_id("peopleamt").send_keys("5")
    my_driver.find_element_by_id("musicquality").send_keys("2")
    my_driver.find_element_by_id("calculate").click()
    return my_driver.find_element_by_id("tip").text


assert calculate_tip(webdriver.Chrome()) == "4.00"
