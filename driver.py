from pyvirtualdisplay import Display
from selenium import webdriver


driver = webdriver.Firefox()


def driver_init():  # setup webdriver and login to target
    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference("dom.webnotifications.enabled", False)
    local_driver = webdriver.Firefox(firefox_profile=_browser_profile)
    display = Display(visible=1, size=[800, 800])
    display.start()
    global driver
    driver = local_driver

