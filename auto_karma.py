from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, getopt
import os
import time

driverPaths = {'Chrome': 'C:\Selenium\chromedriver.exe',
		'Edge': 'C:\Selenium\MicrosoftWebDriver.exe',
		'IE': 'C:\Selenium\IEDriverServer.exe'};

url = 'https://www.hipchat.com/sign_in'
usr = 'thomas.rea@rxpservices.com'
f = open('password.txt','r') #read
passwd = f.read()
message = '@anime++++'
room = {'QA': 'https://rxpservices.hipchat.com/chat/room/4154443',
	'CCA': 'https://rxpservices.hipchat.com/chat/room/3554226',
	'TEST': 'https://rxpservices.hipchat.com/chat/room/4216688'
	};
	
designatedRoom = room['CCA']
	
driver = webdriver.Chrome(driverPaths['Chrome'])
driver.get(url)

xpath = '//*[@id="email"]'
element = driver.find_element_by_xpath(xpath)
element.send_keys(usr)
xpath = '//*[@id="signin"]'
driver.find_element_by_xpath(xpath).click()

xpath = '//*[@id="password"]'
element = driver.find_element_by_xpath(xpath)
element.send_keys(passwd)
xpath = '//*[@id="signin"]'
driver.find_element_by_xpath(xpath).click()

#proceed to web app
xpath = '//*[@id="content"]/div/div/div/div[1]/div/a'
driver.find_element_by_xpath(xpath).click()

#wait for web app to load
driver.implicitly_wait(10)#wait for outlet to load

#select room
driver.get(designatedRoom)

#wait for web app to load
#driver.implicitly_wait(30)#wait for outlet to load
time.sleep(5)

def enterMessage(driver, xpath, message):
	element = driver.find_element_by_xpath(xpath)
	element.send_keys(message)
	time.sleep(0.1)
	element.send_keys(Keys.RETURN)

#enter message
xpath = '//*[@id="hc-message-input"]'

for x in range(0, 99999999):
	enterMessage(driver, xpath, message)
