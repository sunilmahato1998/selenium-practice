import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products'] /div")
count = len(results)
print(count)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# FIX: Wait for promo code field
wait = WebDriverWait(driver, 10)
promo_code_field = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode"))
)
promo_code_field.send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)

print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

driver.quit()