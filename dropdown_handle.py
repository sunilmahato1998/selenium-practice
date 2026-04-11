import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class$='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
# print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"



# Select static dropdown
# Select Options (3 Ways)
#
# By Visible Text
# select.select_by_visible_text("Option Name")
#
# By Value
# select.select_by_value("option_value")
#
# By Index
# select.select_by_index(1)