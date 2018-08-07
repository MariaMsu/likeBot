from driver import driver
from time import sleep


def subscribe_account(link):
    try:
        driver.get(link)
        sleep(1)
        subscribe = driver.find_element_by_xpath("/html/body/span/section/main/div/header/section/div[1]/span/span[1]/button")
        subscribe.click()
    except:
        pass

def insta_task_manager(task_list):
    for task in task_list:
        if task.find("аккаунт") != -1:
            subscribe_account(task[task.find("href=")+6:task.find(">")-1])
