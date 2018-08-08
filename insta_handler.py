from driver import driver
from time import sleep
from datetime import datetime


def debug_screenshot(function_name):
    screenshot_path = "/Users/dovvakkin/github/screenshot_logs/" + function_name + str(
        datetime.now().strftime('%Y_%m_%d_%H:%M:%S')) + ".png"
    driver.save_screenshot(screenshot_path)


def subscribe_account(link):
    try:
        driver.get(link)
        sleep(1)
        subscribe = driver.find_element_by_xpath(
            "/html/body/span/section/main/div/header/section/div[1]/span/span[1]/button")
        subscribe.click()
    except:
        debug_screenshot("INSTA_subscribe_account_")


def insta_task_manager(task_list):
    for task in task_list:
        if task.find("аккаунт") != -1:
            subscribe_account(task[task.find("href=") + 6:task.find(">") - 1])
