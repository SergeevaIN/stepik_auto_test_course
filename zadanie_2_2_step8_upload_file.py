from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    fname = browser.find_element_by_name("firstname")
    fname.send_keys("Test")
	
    lname = browser.find_element_by_name("lastname")
    lname.send_keys("Testov")
	
    email = browser.find_element_by_name("email")
    email.send_keys("test@test.com")
	
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
	
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    
    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(2)