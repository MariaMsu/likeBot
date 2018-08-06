from pyvirtualdisplay import Display
from selenium import webdriver
from Log_in import *


driver = webdriver.Firefox() # webdriver init


display = Display(visible=1, size=[800, 800])
display.start()
target_login(driver)
# vk_login(driver)
driver.get("https://vktarget.ru/list/")