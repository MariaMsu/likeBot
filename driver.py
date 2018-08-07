from pyvirtualdisplay import Display
from selenium import webdriver
from Log_in import *


def init():  # setup webdriver and login to target
    driver = webdriver.Firefox()  # webdriver init
    display = Display(visible=1, size=[800, 800])
    display.start()
    target_login(driver)
    vk_login(driver)
    insta_login(driver)
    fb_login(driver)
    return driver


driver = init()