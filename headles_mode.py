from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")   # latest chrome headless

driver = webdriver.Chrome(options=options)

driver.get("https://google.com")
print(driver.title)

driver.quit()