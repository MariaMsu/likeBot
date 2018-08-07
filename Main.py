import re
from time import sleep  # this should go at the top of the file
import driver
from vk_handler import *


def check_profit():
    while True:
        try:
            print(":)#8======>")
            driver.get("https://vktarget.ru/list/")
            button = driver.find_element_by_xpath('//div[@data-bind="check"]')
            print("(.)(.)")
            button.click()
        except:
            break

def find_tasks(task_list):  # parse task_list for separated social network tasks
    vk_tasks, gplus_tasks, insta_tasks = [], [], []
    for task in task_list:
        if task.find("https://vk.com") != -1:
            vk_tasks.append(task)
        elif task.find("https://www.instagram.com") != -1:
            insta_tasks.append(task)
        elif task.find("https://plus.google.com") != -1:
            gplus_tasks.append(task)

    if vk_tasks:
        vk_task_manager(vk_tasks)
    # if gplus_tasks:
    #     gplus_handler(gplus_tasks)
    # if insta_tasks:
    #     insta_handler(insta_tasks)


def get_task_list():  # parse target for all tasks
    driver.get("https://vktarget.ru/list/")
    sleep(5)  # ВАЖНО
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    task_list = re.findall(r'<a rel="nofollow noopener" data-bind="url" target="_blank" href=".{1,128}</a>', html)
    # TODO:
    print(task_list)

    return (task_list)


#TODO
#time

#find_tasks(get_task_list())
check_profit()
