from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
	
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,'price'),"$100"))
    button = browser.find_element(By.TAG_NAME,"button")
    button.click()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    result = calc(x)
    
    answer = browser.find_element(By.ID,"answer")
    answer.send_keys(result)
    
    submit = browser.find_element(By.ID,"solve")
    submit.click()

finally:
    time.sleep(2)
    