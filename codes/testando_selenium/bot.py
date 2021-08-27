from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(r'D:\Vini\Documents\My_Repository\random_cods\codes\testando_selenium\chromedriver.exe')

browser.get("https://www.google.com/")

input_search = browser.find_element_by_xpath("//input[@type='text']")
input_search.send_keys('python')
# browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
input_search.send_keys(Keys.RETURN)

click_search = browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
click_search.click()
