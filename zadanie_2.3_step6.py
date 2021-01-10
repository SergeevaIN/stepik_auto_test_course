from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    submit = browser.find_element_by_tag_name('button')
    submit.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    result = calc(x)
    
    input = browser.find_element_by_id("answer")
    input.send_keys(result)
    
    confirm = browser.find_element_by_tag_name('button')
    confirm.click()
    
finally:
    time.sleep(2)