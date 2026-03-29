from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

if username is None and password is None and login_button is None:
    print('Элементы не найдены')
else:
    print('Элементы найдены')
