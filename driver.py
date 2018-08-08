from pyvirtualdisplay import Display
from selenium import webdriver
from Log_in import *


def init():  # setup webdriver and login to target
    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(firefox_profile=_browser_profile)
    display = Display(visible=1, size=[800, 800])
    display.start()
    target_login(driver)
    # vk_login(driver)
    # insta_login(driver)
    # fb_login(driver)
    twit_login(driver)
    return driver


driver = init()
