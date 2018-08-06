from selenium import webdriver


VK_LOGIN = '89104696981'
VK_PASSWORD = 'cherep/'

TARGET_LOGIN = "Kozhevnikov.Maria@gmail.com"
TARGET_PASSWORD = "k0zhepnin@"




def vk_login(driver):
    driver.get("https://m.vk.com/")
    textarea = driver.find_element_by_name('email')
    textarea.send_keys(VK_LOGIN)

    textarea = driver.find_element_by_name('pass')
    textarea.send_keys(VK_PASSWORD)

    submit = driver.find_element_by_class_name("fi_row_new")
    submit.click()


def target_login(driver):
    driver.get("https://vktarget.ru")
    text_area = driver.find_element_by_name("username")
    text_area.send_keys(TARGET_LOGIN)

    text_area = driver.find_element_by_name("password")
    text_area.send_keys(TARGET_PASSWORD)

    submit = driver.find_element_by_xpath("//div[@data-login='login']")
    submit.click()
