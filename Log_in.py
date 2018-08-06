from selenium import webdriver


def vk_Login():
    driver = webdriver.Firefox()
    driver.get("https://m.vk.com/")
    textarea = driver.find_element_by_name('email')
    textarea.send_keys('89104696981')

    textarea = driver.find_element_by_name('pass')
    textarea.send_keys('cherep/')

    submit = driver.find_element_by_xpath("//input[@value='Log in']")
    submit.click()