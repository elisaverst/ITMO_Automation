from selenium import webdriver
from selenium.webdriver.common.by import By

def find_elements():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    try:
        username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')

        if username and password and login_button:
            print(f'Элементы найдены')

    except:
        print(f'Элементы не найдены')

    finally:
        driver.quit()

find_elements()
