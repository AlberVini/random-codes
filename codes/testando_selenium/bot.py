from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'D:\Vini\Documents\My_Repository\random_cods\codes\testando_selenium\chromedriver.exe')

browser.get("https://www.google.com/")

input_search = browser.find_element_by_xpath("//input[@type='text']")
input_search.send_keys('python')
input_search.send_keys(Keys.RETURN)
