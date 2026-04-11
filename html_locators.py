import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)

# CSS - tagname[attribute= 'value'] -> //input[@type = 'submit'], #id, .classname
# Form fill karo
driver.find_element(By.NAME, "name").send_keys("Sunil")
driver.find_element(By.NAME, "email").send_keys("sunil@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("pass123")

# Checkbox click karo
driver.find_element(By.ID, "exampleCheck1").click()

# Dropdown select karo
dropdown =Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")


# Radio button click karo (Student)
driver.find_element(By.ID, "inlineRadio1").click()

# Date of Birth fill karo
driver.find_element(By.NAME, "bday").send_keys("01/01/2000")

time.sleep(2)
# Submit button click karo
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

# Submit alert
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
time.sleep(3)
driver.quit()