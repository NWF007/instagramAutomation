from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/?hl=en')

wait = WebDriverWait(driver, 10)
time.sleep(3)
user = driver.find_element_by_name('username')

passw = driver.find_element_by_name('password')

ActionChains(driver)\
    .move_to_element(user).click()\
    .send_keys('username')\  
    .move_to_element(passw).click()\
    .send_keys('password')\  
    .perform()

loginButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
loginButton.click()

time.sleep(3)

notNow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notNow.click()

time.sleep(1)

notificationsNotNow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notificationsNotNow.click()

time.sleep(2)

seeAllSuggestions = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a')
seeAllSuggestions.click()

time.sleep(2)

followButtons = driver.find_elements_by_xpath('//button[contains(.,"Follow")]')

count = 0

for followbtn in followButtons:
        driver.execute_script("arguments[0].click();", followbtn)
        count += 1
        print(count)
        time.sleep(2)

