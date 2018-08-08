from driver import driver
from time import sleep


def subscribe_account(link):
# try:
    driver.get(link)
    sleep(5)
    button = driver.find_element_by_class_name("EdgeButton EdgeButton--secondary EdgeButton--medium button-text follow-text")
    button.click()
# except:
#     pass


def twit_task_manager(task_list):
    for task in task_list:
        if task.find("аккаунт") != -1:
            subscribe_account(task[task.find("href=")+6:task.find(">")-1])


subscribe_account("https://twitter.com/RostecRussia")