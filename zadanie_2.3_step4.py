from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name('button')
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    result = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    
    submit = browser.find_element_by_tag_name("button")
    submit.click()
    
finally:
    time.sleep(2)
