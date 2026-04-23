import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


expected_results = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_result = []
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
    actual_result.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()
assert expected_results == actual_result

driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Wait for page to load
time.sleep(3)

# Scroll down taaki totAmt visible ho
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum_price = 0
for price in prices:
    sum_price += int(price.text)
print(f"Sum: {sum_price}")

# Wait for total amount element
wait = WebDriverWait(driver, 10)
total_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".totAmt"))
)
totalAmount = int(total_element.text)
print(f"Total: {totalAmount}")

assert sum_price == totalAmount

# Promo code
promo_code_field = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode"))
)
promo_code_field.send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)

print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

driver.quit()