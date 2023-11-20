from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#1
driver = webdriver.Chrome()
driver.get("https://ebay.com")
print(driver.title)
driver.quit()

#2
driver = webdriver.Chrome()
driver.get("https://ebay.com")
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("eBay"))
print(driver.title)
driver.quit()

#3
driver = webdriver.Chrome()
driver.get("https://ebay.com")
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("eBay"))
print(driver.title)
search = driver.find_element(By.NAME,"_nkw")
search.send_keys("women watch")
search.send_keys(Keys.RETURN)

driver.quit()

#4
driver = webdriver.Chrome()
driver.get("https://ebay.com")
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("eBay"))
print(driver.title)
search = driver.find_element(By.NAME,"_nkw")
search.send_keys("women watch")
search.send_keys(Keys.RETURN)
#Verify the header contains “results for women watch“
search.submit()
header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'results for women watch')]")))
header_text = header.text
expected_text = "results for women watch"
if expected_text in header_text:
    print("Header contains:", expected_text)
else:
    print("Header does not contain the expected text.")
driver.quit()