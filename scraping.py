from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def pegar_preco(url):

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(5)

    preco = driver.find_element(By.CLASS_NAME, "price")

    valor = preco.text

    driver.quit()

    return valor