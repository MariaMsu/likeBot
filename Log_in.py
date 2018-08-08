from time import sleep
from driver import driver

VK_LOGIN = '89258396534'
VK_PASSWORD = 'k0zhepnin@'

TARGET_LOGIN = "MariaKozevnikov@gmail.com"
TARGET_PASSWORD = "k0zhepnin@"

FB_LOGIN = '89258396534'
FB_PASSWORD = 'k0zhepnin@'

INSTA_LOGIN = 'maria.kozevnikov'
INSTA_PASSWORD = 'k0zhepnin@'

TWIT_LOGIN = '89258396534'
TWIT_PASSWORD = 'k0zhepnin@'



def vk_login():
    driver.get("https://m.vk.com/")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(VK_LOGIN)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(VK_PASSWORD)

    submit = driver.find_element_by_class_name("fi_row_new")
    submit.click()


def fb_login():
    driver.get("https://www.facebook.com")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(FB_LOGIN)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(FB_PASSWORD)

    submit = driver.find_element_by_id('loginbutton')
    submit.click()


def twit_login():
    driver.get("https://twitter.com/login")
    sleep(1)
    try:
        text_area = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
        text_area.send_keys(TWIT_LOGIN)

        text_area = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
        text_area.send_keys(TWIT_PASSWORD)

        submit = driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()
    except:
        text_area = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
        text_area.send_keys(TWIT_LOGIN)

        text_area = driver.find_element_by_xpath("//input[@name='session[password]']")
        text_area.send_keys(TWIT_PASSWORD)

        submit = driver.find_element_by_xpath("//div[text()='Войти']")
        submit.click()


def insta_login():
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(3)
    text_area = driver.find_element_by_name("username")
    text_area.send_keys(INSTA_LOGIN)

    text_area = driver.find_element_by_name('password')
    text_area.send_keys(INSTA_PASSWORD)

    submit = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/span/button")
    submit.click()
    sleep(2)


def target_login():
    driver.get("https://vktarget.ru")
    text_area = driver.find_element_by_name("username")
    text_area.send_keys(TARGET_LOGIN)

    text_area = driver.find_element_by_name("password")
    text_area.send_keys(TARGET_PASSWORD)

    submit = driver.find_element_by_xpath("//div[@data-login='login']")
    submit.click()


def general_login():
    target_login()
    vk_login()
    insta_login()
    fb_login()
    twit_login()
