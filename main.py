import time
import credentials

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FName = credentials.firstName
LName = credentials.lastName
PNum = credentials.phoneNumber
UCREmail = credentials.ucrEmail
SID = credentials.SID



driver = webdriver.Chrome()
# opens up the google link
driver.get("https://university-of-california-riverside.app.qless.com/kiosk/5dbe4d31-50f2-4013-b4c7-eab37e244442?locale=en")

# wait for page to load 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/main/div/button'))
)

# start button
start_button = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')

#click button
start_button.click()

# wait for next page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="kiosk-wizard-container"]/div[1]/div/div[1]/button'))
)

# find meal support button
meal_support_button = driver.find_element(By.XPATH, '//*[@id="kiosk-wizard-container"]/div[1]/div/div[1]/button')

# click meal support button
meal_support_button.click()

#wait for next page to load

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="46df6d66-ba6a-47c8-96cd-ebba5f014f9e"]/div[2]/div[3]/div/button'))
)

# find the joint waitlist button 
join_waitlist_button = driver.find_element(By.XPATH, '//*[@id="46df6d66-ba6a-47c8-96cd-ebba5f014f9e"]/div[2]/div[3]/div/button')

join_waitlist_button.click()

# Fill out information now

# wait for page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="First Name"]'))
)

# first name
firstNameTB = driver.find_element(By.XPATH, '//*[@id="First Name"]')
firstNameTB.send_keys(FName)

# last name
lastNameTB = driver.find_element(By.XPATH, '//*[@id="Last Name"]')
lastNameTB.send_keys(LName)

# country code

# phone number
phoneNumberTB = driver.find_element(By.XPATH, '//*[@id="Phone Number"]')
phoneNumberTB.send_keys(PNum)

#ucr email
ucrEmailTB = driver.find_element(By.XPATH, '//*[@id="Email"]')
ucrEmailTB.send_keys(UCREmail)

#student id
studentIDTB = driver.find_element(By.XPATH, '//*[@id="Student ID"]')
studentIDTB.send_keys(SID)

#terms of agreement yes
TOA_button  = driver.find_element(By.XPATH, '//*[@id="terms_conditions"]')
TOA_button.click()

# submit waitlist form
submit_information_button = driver.find_element(By.XPATH, '//*[@id="contact-details-continue-btn"]')
submit_information_button.click()


# new page
# - confirm button
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="kiosk-wizard-container"]/div[3]/div/button'))
)

confirm_button = driver.find_element(By.XPATH, '//*[@id="kiosk-wizard-container"]/div[3]/div/button')
confirm_button.click()

# done
time.sleep(99)

driver.quit()

# XPATHS