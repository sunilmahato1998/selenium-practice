import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# ============ CHECKBOX ============
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(f"✅ Checkboxes: {len(checkboxes)}")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        print("✅ Checkbox 'option2' selected")
        break

# ============ RADIO BUTTON (BEST METHOD) ============
# Direct select by value - No index confusion!
radio2 = driver.find_element(By.CSS_SELECTOR, "input[value='radio2']")
radio2.click()
assert radio2.is_selected()
print("✅ Radio 'radio2' selected")

time.sleep(2)

# ============ DISPLAY/HIDE ============
assert driver.find_element(By.ID, "displayed-text").is_displayed()
print("✅ Text displayed")

driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
print("✅ Text hidden")


# ======================== JAVA ALERT ===============================
name = "Sunil Kumar"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
alert.accept()
# alert.dismiss()
print(alertText)
assert name in alertText

# driver.quit()
print("\n✅✅✅ All tests passed! ✅✅✅")

