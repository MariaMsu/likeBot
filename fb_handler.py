from driver import driver
from time import sleep
from datetime import datetime


def debug_screenshot(function_name):
    screenshot_path = "/Users/dovvakkin/github/screenshot_logs/" + function_name + str(
        datetime.now().strftime('%Y_%m_%d_%H:%M:%S')) + ".png"
    driver.save_screenshot(screenshot_path)


def like_on_page(link):
    try:
        driver.get(link)
        page = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/button")
        page.click()
    except:
        debug_screenshot("FB_like_on_page_")


def fb_task_manager(task_list):
    for task in task_list:
        if task.find("странице") != -1:
            like_on_page(task[task.find("href=")+6:task.find(">")-1])



