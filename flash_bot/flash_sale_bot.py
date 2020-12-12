# Flash Sale Bot for Shopee
# mariobgsp

# install python 3.8.3: https://www.python.org/downloads/release/python-383/
# open cmd then type: pip install selenium
# install chromedriver in https://chromedriver.chromium.org/


# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time 

PATH = "D:/bot_gabut/chromedriver.exe" 
# Please be mind your path directory chromedriver.exe  
driver = webdriver.Chrome(PATH)

# Login Credentials
email = "email saya"
password = "password saya"

# Shopeee HTML
login_link = "https://shopee.co.id/buyer/login" # Login Page

# Product Link #With Product Link Example
product_link = "https://shopee.co.id/V8-Full-Hd-Webcam-1080P-With-Microphone-Web-cam-FULL-HD-1080-P-i.61050481.3238894052"

# BOT START 
driver.get(login_link)

time.sleep(3)

# inputing login credentials
user = driver.find_element_by_class_name('_56AraZ')
user.send_keys(email) # input email put it between a string ''

time.sleep(1) # wait to load 3s, if you want it faster, you should reduce the number,
              # but it depends on your internet speed

pwd = driver.find_element_by_xpath("//input[@name='password']")
pwd.send_keys(password) # input password put it between string ''

time.sleep(1) # wait to load 3s, if you want it faster, you should reduce the number,
              # but it depends on your internet speed 

# automatically click login button
login_button = driver.find_element_by_xpath("//button[@class='_35rr5y _32qX4k _1ShBrl _3z3XZ9 _2iOIqx _2h_2_Y']")
login_button.click()

time.sleep(2) #OTP Time, you can set it to longer time and input your OTP manually, 
              # or you just can disable OTP from shopee settings 

# Buy buy buy
driver.get(product_link)

time.sleep(2) # wait to load

buy_out = driver.find_element_by_xpath("//button[@class='btn btn-solid-primary btn--l YtgjXY']")
buy_out.click()

# Done, You should checkout manually