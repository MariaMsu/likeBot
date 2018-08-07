VK_LOGIN = '89258396534'
VK_PASSWORD = 'k0zhepnin@'

TARGET_LOGIN = "MariaKozevnikov@gmail.com"
TARGET_PASSWORD = "k0zhepnin@"

FB_LOGIN = '89258396534'
FB_PASSWORD = 'k0zhepnin@'

INSTA_LOGIN = 'maria.kozevnikov'
INSTA_PASSWORD = 'k0zhepnin@'


def vk_login(driver):
    driver.get("https://m.vk.com/")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(VK_LOGIN)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(VK_PASSWORD)

    submit = driver.find_element_by_class_name("fi_row_new")
    submit.click()


def fb_login(driver):
    driver.get("https://www.facebook.com")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(FB_LOGIN)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(FB_PASSWORD)

    submit = driver.find_element_by_id('loginbutton')
    submit.click()


def insta_login(driver):
    driver.get("https://www.instagram.com/accounts/login/")
    text_area = driver.find_element_by_name("username")
    text_area.send_keys(INSTA_LOGIN)

    text_area = driver.find_element_by_name("password")
    text_area.send_keys(INSTA_PASSWORD)

    submit = driver.find_element_by_class_name("_5f5mN jIbKX KUBKM yZn4P ")
    submit.click()



def target_login(driver):
    driver.get("https://vktarget.ru")
    text_area = driver.find_element_by_name("username")
    text_area.send_keys(TARGET_LOGIN)

    text_area = driver.find_element_by_name("password")
    text_area.send_keys(TARGET_PASSWORD)

    submit = driver.find_element_by_xpath("//div[@data-login='login']")
    submit.click()
